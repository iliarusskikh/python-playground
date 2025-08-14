from transformers import pipeline
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

# Path to your context.pdf file
pdf_path = "context.pdf"

# Extract context from the PDF
context = extract_text_from_pdf(pdf_path)

# Initialize the question-answering pipeline
question_answerer = pipeline("question-answering")

# Perform question answering
if context:
    result = question_answerer(
        question="Tell me about frequency hopping?",
        context=context
    )
    print(result)
else:
    print("No context available from the PDF.")
