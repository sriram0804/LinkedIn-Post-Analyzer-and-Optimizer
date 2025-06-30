# 📢 LinkedIn Post Analyzer & Optimizer

A full-stack AI-powered web application that analyzes and optimizes your LinkedIn post drafts. Users can paste their content and receive:

- ✅ **Sentiment analysis**
- ✅ **Keyword extraction (NLP-based)**
- ✅ **Readability scoring**
- ✅ **GPT-powered rewriting suggestions** to boost post engagement

> ✨ Built with React, Flask, and OpenAI GPT — demonstrates real-world marketing tech & AI integration.

---

## 🚀 Features

- 📊 **Sentiment Score:** Analyze positivity/negativity of your post
- 🧠 **Keyword Suggestions:** NLP-extracted core keywords
- 📖 **Readability Score:** Evaluated via `textstat`
- ✍️ **AI Rewrite Button:** Generates a more engaging version of your post using GPT
- 💻 **Modern UI:** Built with React + Vite + TailwindCSS

---

## 🧰 Tech Stack

| Frontend       | Backend        | ML/NLP | API/AI |
|----------------|----------------|--------|--------|
| React (Vite)   | Flask + Python | NLTK, TextBlob, TextStat, KeyBERT | OpenAI GPT-3.5 Turbo |

---

## 📁 Directory Structure

linkedin-post-optimizer/
├── backend/
│ ├── app.py
│ ├── .env # Contains your OpenAI API key
│ ├── requirements.txt # Backend dependencies
│ └── venv/ # Python virtual environment (Set your OPENAPI KEY here)
└── frontend/
├── src/
│ ├── App.jsx
│ ├── components/
│ │ ├── InputCard.jsx
│ │ ├── ResultCard.jsx
│ │ └── RewriteCard.jsx
│ └── index.css
├── vite.config.js
└── package.json

## 🔒 Security Notes
.env is excluded via .gitignore to protect your API key.

CORS is enabled via flask-cors for development access.

## 🧠 Models & Libraries Used
TextBlob – for sentiment analysis

KeyBERT – for keyword extraction

TextStat – for readability

OpenAI GPT – for content rewriting (via ChatGPT API)

## 🙌 Acknowledgments
OpenAI for GPT APIs

KeyBERT & TextStat community

React, Flask, Tailwind contributors

## 💡 Future Improvements
User authentication

Post scheduling for LinkedIn

Post performance prediction (engagement scoring)

** Note to Create a .env file and paste your OPEN API Key "OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx" **

