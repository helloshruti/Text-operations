from flask import Flask, render_template, request
from textblob import TextBlob
from googletrans import Translator
import summarizer

app = Flask(__name__)

translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    operation = request.form['operation']
    text = request.form['text']
    
    if operation == 'translate':
        dest_lang = request.form['dest-lang']
        translated = translator.translate(text, dest=dest_lang)
        return f"Translated Text: {translated.text}"

    elif operation == 'summarize':
        summary = summarizer.summarize_text(text)  # assuming you have a function in summarizer.py
        return f"Summary: {summary}"

    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(debug=True)
