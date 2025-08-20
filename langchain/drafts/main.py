#chainlit run app.py -w
#pip install aiohttp==3.9.0
# import chainlit as cl

# from langchain.memory import ChatMessageHistory, ConversationBufferMemory


# @cl.on_chat_start
# async def start():
#     # files = None
#     # while files is None:
#     #     files = await cl.AskFileMessage(
#     #         content=welcome_message,
#     #         accept=["text/plain", "application/pdf"],
#     #         max_size_mb=20,
#     #         timeout=180,
#     #     ).send()

#     # file = files[0]

#     # msg = cl.Message(content=f"Processing `{file.name}`...", disable_feedback=True)
#     # await msg.send()

#     # # No async implementation in the Pinecone client, fallback to sync
#     # docsearch = await cl.make_async(get_docsearch)(file)

#     message_history = ChatMessageHistory()

#     memory = ConversationBufferMemory(
#         memory_key="chat_history",
#         output_key="answer",
#         chat_memory=message_history,
#         return_messages=True,
#     )

#     # chain = ConversationalRetrievalChain.from_llm(
#     #     ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True),
#     #     chain_type="stuff",
#     #     retriever=docsearch.as_retriever(),
#     #     memory=memory,
#     #     return_source_documents=True,
#     # )

#     # # Let the user know that the system is ready
#     # msg.content = f"`{file.name}` processed. You can now ask questions!"
#     # await msg.update()

#     #cl.user_session.set("chain", chain)




# @cl.on_message
# async def main(message: cl.Message):
#     # Your custom logic goes here...

#     # Send a response back to the user
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()
    


from operator import itemgetter

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import Runnable, RunnablePassthrough, RunnableLambda
from langchain.schema.runnable.config import RunnableConfig
from langchain.memory import ConversationBufferMemory

from chainlit.types import ThreadDict
import chainlit as cl


def setup_runnable():
    memory = cl.user_session.get("memory")  # type: ConversationBufferMemory
    model = ChatOpenAI(streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful chatbot"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    runnable = (
        RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        )
        | prompt
        | model
        | StrOutputParser()
    )
    
    # Store the runnable in user session
    cl.user_session.set("runnable", runnable)
    return runnable


@cl.password_auth_callback
def auth(user_name: str, password: str):
    # Check if the username and password match
    if user_name == "user" and password == "12345":
        return cl.User(identifier="user")
    else:
        return None


@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="GPT-3.5",
            markdown_description="The underlying LLM model is **GPT-3.5**.",
            icon="https://picsum.photos/200",
        ),
        # cl.ChatProfile(
        #     name="GPT-4",
        #     markdown_description="The underlying LLM model is **GPT-4**.",
        #     icon="https://picsum.photos/250",
        # ),
    ]

@cl.on_chat_start
async def on_chat_start():
    #chat_profile = cl.user_session.get("chat_profile")

    cl.user_session.set("memory", ConversationBufferMemory(return_messages=True))
    setup_runnable()


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    memory = ConversationBufferMemory(return_messages=True)
    root_messages = [m for m in thread["steps"] if m["parentId"] == None]
    for message in root_messages:
        if message["type"] == "user_message":
            memory.chat_memory.add_user_message(message["output"])
        else:
            memory.chat_memory.add_ai_message(message["output"])

    cl.user_session.set("memory", memory)
    setup_runnable()


# Test function to verify chat memory works
@cl.on_message
async def test_memory(message: cl.Message):
    # This function can be used to test memory by sending a message like "What was our previous conversation?"
    # Or you can manually send messages in the chat and observe if the AI remembers context

    # Example test logic:
    if "test memory" in message.content.lower():
        memory = cl.user_session.get("memory")
        history = memory.load_memory_variables({})
        await cl.Message(content=f"Memory contains: {history}").send()
    else:
        # Default behavior - process the message normally
        try:
            memory = cl.user_session.get("memory")  # type: ConversationBufferMemory
            runnable = cl.user_session.get("runnable")  # type: Runnable

            if not runnable:
                raise Exception("Runnable not initialized")

            res = cl.Message(content="")

            async for chunk in runnable.astream(
                {"question": message.content},
                config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
            ):
                await res.stream_token(chunk)

            await res.send()

            # Add messages to memory after successful response
            memory.chat_memory.add_user_message(message.content)
            memory.chat_memory.add_ai_message(res.content)

        except Exception as e:
            # Handle errors gracefully
            error_msg = cl.Message(content=f"Error: {str(e)}")


### How to Test Chat Memory:
# 1. **Start a conversation**: Send several messages in sequence.
# 2. **Ask about context**: Ask questions like "What did we talk about earlier?" or "Can you summarize our last discussion?"
# 3. **Check memory manually**: Send a message like "test memory" to see the current memory contents.
# 4. **Resume chat**: Close and reopen the chat window to verify that conversation history is preserved.


