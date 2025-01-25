from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# RapidAPI configuration (from .env)
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "horoscopeapi-horoscope-v1.p.rapidapi.com"
API_URL = "https://horoscopeapi-horoscope-v1.p.rapidapi.com/daily"

def get_horoscope(sign, date="today"):
    """Fetch horoscope data from the API"""
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    params = {
        "date": date,
        "sign": sign.lower()  # Ensure lowercase for API compatibility
    }
    
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    horoscope = None
    error = None
    
    if request.method == "POST":
        zodiac_sign = request.form.get("zodiac_sign")
        selected_date = request.form.get("date", "today")  # Default to 'today'
        
        # Validate input
        if not zodiac_sign:
            error = "Please select a zodiac sign."
        else:
            horoscope = get_horoscope(zodiac_sign, selected_date)
            if not horoscope:
                error = "Failed to fetch horoscope. Please try again later."
    
    return render_template(
        "index.html",
        horoscope=horoscope,
        error=error,
        zodiac_sign=request.form.get("zodiac_sign", "scorpio")  # Default to Scorpio
    )

if __name__ == "__main__":
    app.run(debug=True)