from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# New API Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "daily-horoscope-advanced-api.p.rapidapi.com"
API_URL = "https://daily-horoscope-advanced-api.p.rapidapi.com/api/Daily-Horoscope-New/"

def get_horoscope(zodiac_sign, time_period="daily"):
    """Fetch horoscope from the new advanced API"""
    try:
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": RAPIDAPI_HOST
        }
        
        params = {
            "zodiacSign": zodiac_sign.capitalize(),  # API expects capitalized signs
            "timePeriod": time_period.lower()        # daily/weekly/monthly
        }
        
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        
        # Debug: Print the API response
        print("API Response:", response.json())
        
        return response.json()
        
    except Exception as e:
        print(f"API Error: {str(e)}")
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    horoscope = None
    error = None
    zodiac_sign = "leo"  # Default sign
    time_period = "daily"  # Default period
    
    if request.method == "POST":
        zodiac_sign = request.form.get("zodiac_sign", "leo")
        time_period = request.form.get("time_period", "daily")
        
        # Fetch horoscope from API
        horoscope = get_horoscope(zodiac_sign, time_period)
        
        # Debug: Use hardcoded data if API fails or returns invalid data
        if not horoscope:
            error = "Failed to fetch horoscope. Please try again later."
            horoscope = {
                "horoscope": "Today is a great day for Leos!",
                "mood": "Happy",
                "compatibility": "Gemini",
                "lucky_number": "7"
            }
        elif "message" in horoscope:  # Handle API error messages
            error = horoscope.get("message")
            horoscope = {
                "horoscope": "No prediction available.",
                "mood": "N/A",
                "compatibility": "N/A",
                "lucky_number": "N/A"
            }

    return render_template(
        "index.html",
        horoscope=horoscope,
        error=error,
        zodiac_sign=zodiac_sign,
        time_period=time_period
    )

if __name__ == "__main__":
    app.run(debug=True)