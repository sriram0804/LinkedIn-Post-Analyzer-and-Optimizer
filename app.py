from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
from textstat import flesch_reading_ease
from keybert import KeyBERT
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

kw_model = KeyBERT()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    sentiment_score = TextBlob(text).sentiment.polarity
    sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    keywords = [kw[0] for kw in kw_model.extract_keywords(text, stop_words='english', top_n=5)]
    readability = flesch_reading_ease(text)

    return jsonify({
        'sentiment_score': round(sentiment_score, 2),
        'sentiment_label': sentiment_label,
        'keywords': keywords,
        'readability': round(readability, 2)
    })

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.get_json()
    text = data.get('text', '')

    prompt = f"Rewrite the following LinkedIn post to make it more engaging and professional:\n\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that improves LinkedIn posts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    improved = response['choices'][0]['message']['content'].strip()
    return jsonify({ 'rewrite': improved })

if __name__ == '__main__':
    app.run(debug=True)
