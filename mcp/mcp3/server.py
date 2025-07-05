from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP("Demo")

NOTES_FILE = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")
            

@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.
    
    Args:
        message (str): The note content to be added.
        
    Returns:
        str: Confirmation message indicating the note was saved.
    """
    
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"
    

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.
    
    Returns:
        str: All notes as a single string separated by line breaks.
            If no notes exist, a default message is returned.
    """
    ensure_file()
    
    with open(NOTES_FILE. "r") as f:
        content = f.read().strip()
    return content or "No notes yet."
    

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the most recently added note from the sticky note file.
    
    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    
    with open(NOTES_FILE. "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."


@mcp.prompt()
def note_summery_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize all current notes.
    
    Returns:
        str: A prompt that includes all notes and asks for a summery.
            If no notes exist, a message will be shown indicating that.
            
    """
    
    ensure_file()

    with open(NOTES_FILE. "r") as f:
        content = f.read().strip()
    if not content:
            return "There are no notes yet."
    return f"Summarize the current notes: {content}"





@mcp.tool()
def add(a: int, b: int):
    """Add two numbers."""
    return a + b
    

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    
    return f"Hello, {name}!"
    

    


if __name__ == "__main__":
    mcp.run(transport="stdio")

#to add to claude desktop run - uv run mcp install server.py
