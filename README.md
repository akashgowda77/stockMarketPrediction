🚀 Stock Market Prediction & Analysis Platform

A full-stack, ML-powered web application for analyzing Indian stock markets, predicting trends, and managing personalized watchlists in real time.

🌟 Overview

This project is designed to simulate a real-world fintech analytics platform. It combines data engineering, machine learning, and full-stack development to deliver actionable insights on stock market behavior.

Users can track live stock data, visualize trends, and generate predictions using statistical models — all within a clean, interactive interface.

🔥 Key Highlights
⚡ Real-time stock data integration (NSE/BSE)
📊 ML-based price prediction (Linear Regression)
📈 Technical indicators (Bollinger Bands)
🔐 Secure authentication system
⭐ Personalized watchlist dashboard
🧠 Data-driven decision support
🌐 Fully deployed cloud application
🧠 Problem Statement

Retail investors often lack access to:

Simple tools for analyzing stock trends
Affordable predictive insights
Personalized tracking systems

This project solves that by providing a centralized intelligent platform for:

Monitoring stocks
Understanding trends
Making informed decisions
🛠️ Tech Stack
💻 Backend
Flask
Flask-PyMongo
Flask-Limiter
🧠 Machine Learning
scikit-learn (Linear Regression)
📊 Data Processing
pandas
numpy
yfinance
🗄️ Database
MongoDB Atlas
☁️ Deployment
Render (Cloud Platform)
⚙️ System Architecture
User → Flask App → ML Model → MongoDB → Response (UI)
                ↓
          Yahoo Finance API
🚀 Features in Detail
📡 Real-Time Data Fetching
Retrieves live stock data using Yahoo Finance API
Supports NSE & BSE stocks
📉 Price Prediction
Uses Linear Regression model
Predicts future stock trends based on historical data
📊 Technical Analysis
Bollinger Bands for volatility analysis
Helps identify overbought/oversold conditions
🔐 Authentication System
Secure login/signup
Password hashing using industry standards
⭐ Watchlist Management
Add/remove stocks
Personalized tracking dashboard
📊 Market Overview

Tracks major indices:

NIFTY 50
SENSEX
NIFTY BANK
INDIA VIX
📰 Financial News Integration
Aggregates latest stock-related news
📂 Project Structure
stockMarketPrediction/
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── .env.example
├── css/
├── templates/
└── test_*.py
⚙️ Local Setup
1️⃣ Clone Repository
git clone https://github.com/akashgowda77/stockMarketPrediction.git
cd stockMarketPrediction
2️⃣ Create Virtual Environment
python -m venv .venv

Activate:

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment
cp .env.example .env

Add:

MONGO_URI
SECRET_KEY
5️⃣ Run Application
python app.py

Visit:

http://localhost:5003
🌐 Deployment (Render)
Configuration
Runtime: Python 3
Build:
pip install -r requirements.txt
Start:
gunicorn app:app
Environment Variables
Key	Description
MONGO_URI	MongoDB connection
SECRET_KEY	Session security
🔐 Security Implementation
Password hashing (pbkdf2:sha256)
API rate limiting
Secure HTTP headers
MongoDB TLS encryption
📈 Future Enhancements
🔮 Advanced ML models (LSTM, ARIMA)
📊 Interactive charts (Plotly)
📱 Mobile-responsive UI improvements
🔔 Price alerts & notifications
📉 Portfolio performance tracking
💼 Why This Project Stands Out

This project demonstrates:

✅ Full-stack development skills
✅ Real-world ML integration
✅ API handling & data pipelines
✅ Secure authentication systems
✅ Cloud deployment experience

👉 It reflects the kind of system used in fintech products and trading platforms
