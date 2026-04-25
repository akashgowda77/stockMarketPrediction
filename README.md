# STOCK MARKET PREDICTION

A Flask-based web application for analyzing Indian stock market data, predicting trends, and managing personalized watchlists.

## Features

- Real-time stock data fetching (NSE/BSE via Yahoo Finance)
- Machine learning-based price prediction using Linear Regression with Bollinger Bands
- Secure user authentication with MongoDB-backed sessions
- Personal watchlist management
- Market indices tracking (NIFTY 50, SENSEX, NIFTY BANK, INDIA VIX)
- Sector-wise stock exploration
- Financial news aggregation

## Tech Stack

- **Backend:** Flask, Flask-PyMongo, Flask-Limiter
- **Database:** MongoDB Atlas
- **ML:** scikit-learn (Linear Regression)
- **Data:** yfinance, pandas, numpy
- **Deployment:** Render (Web Service)

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/akashgowda77/stockMarketPrediction.git
cd stockMarketPrediction
```
### 2. Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure environment variables

```bash
cp .env.example .env
```
Edit `.env` and fill in your actual values:

- **MONGO_URI**: Your MongoDB Atlas connection string
- **SECRET_KEY**: A strong random string (generate with `python -c "import secrets; print(secrets.token_hex(32))"`)

### 5. Run the app

```bash
python app.py
```

The app will be available at `http://localhost:5003`

## Deploy to Render

### Prerequisites

- A [Render](https://render.com) account
- Your MongoDB Atlas cluster configured with **Network Access** set to `Allow access from anywhere` (or Render's outbound IPs)

### Steps

1. **Push your code to GitHub** (already done if you're reading this)

2. **Create a new Web Service on Render:**
   - Go to [dashboard.render.com](https://dashboard.render.com)
   - Click **New +** → **Web Service**
   - Connect your GitHub repository: `akashgowda77/stockMarketPrediction`

3. **Configure the service:**
   - **Name:** `stock-prediction` (or your preference)
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

4. **Set Environment Variables:**
   In the Render dashboard, go to **Environment** and add:

   | Key | Value |
   |-----|-------|
   | `MONGO_URI` | Your MongoDB Atlas connection string |
   | `SECRET_KEY` | A strong random string (generate locally with Python `secrets.token_hex(32)`) |

5. **Deploy:**
   Click **Create Web Service**. Render will build and deploy automatically.

### Important Notes for Render Deployment

- **Do NOT commit `.env` to GitHub** — it is already in `.gitignore`
- **Do NOT expose your MongoDB credentials** in code or logs
- Render automatically sets `PORT` — the app listens on `os.getenv('PORT', 5003)`
- The free tier may have cold starts (~30s delay after inactivity)

## Project Structure

```
STOCK_PREDICTION/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies (pinned versions)
├── runtime.txt            # Python version for Render
├── Procfile               # Process definition for Render
├── .env.example           # Environment variable template
├── .gitignore
├── css/                   # Static stylesheets
├── templates/             # Jinja2 HTML templates
└── test_*.py              # Unit tests
```

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `MONGO_URI` | Yes | MongoDB connection string |
| `SECRET_KEY` | Yes | Flask session encryption key |
| `PORT` | No | Server port (default: 5003) |

## Security

- Passwords are hashed with `pbkdf2:sha256`
- Rate limiting enabled on auth and API endpoints
- Security headers (`X-Frame-Options`, `X-Content-Type-Options`, etc.)
- MongoDB TLS/SSL certificate verification via `certifi`

📈 Future Improvements
- Advanced ML models (LSTM, ARIMA)
- Interactive charts (Plotly)
- Portfolio tracking system
- Price alerts & notifications
- Mobile responsive UI

💼 Project Impact
This project demonstrates:
- Full-stack development skills
- Machine learning integration
- Real-time API handling
- Secure authentication systems
- Cloud deployment experience
