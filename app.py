from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# Personal Information
personal_info = {
    "name": "Irfan Rahaman",
    "age": 21,
    "email": "irfanrahaman324@gmail.com",
    "github": "https://github.com/Irfanrahaman",
    "linkedin": "https://linkedin.com/in/irfanrahaman",
    "fiverr": "https://fiverr.com/irfanrahaman",
    "skills": ["AI", "Machine Learning", "Cloud Computing", "Computer Vision"],
    "hire_link": "mailto:irfanrahaman324@gmail.com",
    "instagram": "https://www.instagram.com/irfanrahaman8420?igsh=aThjbDBhb3ZlM2Nm", # Added Instagram link
    "facebook": "https://www.facebook.com/share/14Doh2cEk5g/", # Added Facebook link
    "phone": "+91 8420193467", # Existing phone number
}

# Projects
projects = [
    {
        "title": "AI Chatbot",
        "description": "A conversational chatbot for task automation and customer support.",
        "link": "https://github.com/Irfanrahaman/chatbot-ai",
    },
    {
        "title": "Customer Churn Prediction",
        "description": "Machine learning model for predicting customer churn using convolution.",
        "link": "https://github.com/Irfanrahaman/customer-churn-prediction",
    },
    {
        "title": "Invoice Data Extractor",
        "description": "OCR-based parser for extracting structured data from scanned invoices.",
        "link": "https://github.com/Irfanrahaman/ocr-ai-project",
    },
    {
        "title": "AI E-Commerce Recommender",
        "description": "An AI-powered system to provide personalized product recommendations for e-commerce platforms.",
        "link": "https://github.com/Irfanrahaman/AI--ECommerce-Recommender",
    },
]

# Certificates
certificates = [
    {"name": "Intro to Deep Learning", "link": "https://www.kaggle.com/certificate/placeholder1"},
    {"name": "Intermediate Machine Learning", "link": "https://www.kaggle.com/certificate/placeholder2"},
    {"name" : "Intro to Machine Learning", "link" : "https://www.kaggle.com/learn/certification/irfanrahaman/intro-to-deep-learning"},
    {"name" : "Data cience & Analytics", "link" : "https://www.life-global.org/certificate/6f7310e8-a0e9-46e1-94b9-e04af8a98e26"},
]

@app.route('/')
def index():
    return render_template('index.html', personal=personal_info, projects=projects, certificates=certificates)

@app.route('/resume')
def download_resume():
    try:
        return send_from_directory(
            directory='static/resume',
            path='irfan_resume.pdf',
            as_attachment=True
        )
    except FileNotFoundError:
        abort(404, description="Resume file not found.")

@app.errorhandler(404)
def page_not_found(e):
    return {"error": str(e)}, 404

@app.errorhandler(500)
def internal_server_error(e):
    return {"error": "Internal Server Error"}, 500

if __name__ == '__main__':
    app.run(debug=True)