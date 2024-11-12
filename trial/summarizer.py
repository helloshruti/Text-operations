from transformers import pipeline

# Load the BART summarization model
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(content):
    # Generate a summary
    summary = summarization_pipeline(content, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return summary
