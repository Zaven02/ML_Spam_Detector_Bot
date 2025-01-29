from transformers import pipeline

# Load the spam detection model
pipe = pipeline("text-classification", model="dima806/email-spam-detection-distilbert")

def spam_classifier(text: str):
    return pipe(text)
