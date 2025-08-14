import ollama
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + " "
            return text.strip()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

# Path to your context.pdf file
pdf_path = "context.pdf"

# Extract context from the PDF
context = extract_text_from_pdf(pdf_path)

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the question
model = "mistral"  # Replace with your model name
question = "What are communication protocols of EX600-W?"

# Create a prompt that includes the PDF context and the question
if context:
    prompt = f"Based on the following context, answer the question:\n\nContext: {context}\n\nQuestion: {question}"
else:
    prompt = f"No context available from the PDF. Please answer the question directly: {question}"

# Send the query to the model
try:
    response = client.generate(model=model, prompt=prompt)
    # Print the response from the model
    print("Response from Ollama:")
    print(response.response)
except Exception as e:
    print(f"Error querying Ollama: {e}")
