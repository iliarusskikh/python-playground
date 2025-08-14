#huggingface notes

#where the models are
#~/.cache/huggingface/hub/
#rm -rf ~/.cache/huggingface/hub/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english
#rm -rf ~/.cache/huggingface/hub/*

#pip3 install huggingface_hub
#huggingface-cli scan-cache
#huggingface-cli delete-cache

#pip install "transformers[sentencepiece]"

#Virtual Environment!
#python -m venv .env
# Activate the virtual environment
#source .env/bin/activate

# Deactivate the virtual environment
#deactivate


#pipeline()


# def main():
#     print("Hello from huggingface-practice!")




# if __name__ == "__main__":
#     main()

# from transformers import pipeline

# classifier = pipeline("sentiment-analysis")
# result = classifier(["I've been waiting for a HuggingFace course my whole life.","The door is mango"])
# print(result)

# from transformers import pipeline

# classifier = pipeline("zero-shot-classification")
# result = classifier(
#     "This is a course about the Transformers library",
#     candidate_labels=["education", "politics", "business"],
# )
# print(result)


# generator = pipeline("text-generation")
# generator("In this course, we will teach you how to")

# generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")
# generator(
#     "In this course, we will teach you how to",
#     max_length=30,
#     num_return_sequences=2,
# )

# question_answerer = pipeline("question-answering")
# question_answerer(
#     question="Where do I work?",
#     context="My name is Sylvain and I work at Hugging Face in Brooklyn",
# )

# Text pipelines
# text-generation: Generate text from a prompt
# text-classification: Classify text into predefined categories
# summarization: Create a shorter version of a text while preserving key information
# translation: Translate text from one language to another
# zero-shot-classification: Classify text without prior training on specific labels
# feature-extraction: Extract vector representations of text
# Image pipelines
# image-to-text: Generate text descriptions of images
# image-classification: Identify objects in an image
# object-detection: Locate and identify objects in images
# Audio pipelines
# automatic-speech-recognition: Convert speech to text
# audio-classification: Classify audio into categories
# text-to-speech: Convert text to spoken audio
# Multimodal pipelines
# image-text-to-text: Respond to an image based on a text prompt


# from transformers import pipeline

# translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
# translator("Привет! Как насчет сходить в кино на новых Звездные Войны!")

#Question answering (extractive)	Encoder	BERT, RoBERTa




# from transformers import AutoModel

# model = AutoModel.from_pretrained("bert-base-cased")
# print(model)

from datasets import load_dataset

raw_datasets = load_dataset("squad")