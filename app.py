import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# List of valid zodiac signs and time periods
VALID_ZODIAC_SIGNS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo", 
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]
VALID_TIME_PERIODS = ["today", "yesterday", "tomorrow"]

def fetch_horoscope(zodiac_sign, time_period):
    """Fetch horoscope data from the Aztro API."""
    try:
        response = requests.post(
            f"https://aztro.sameerkumar.website/?sign={zodiac_sign}&day={time_period}"
        )
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, "Failed to fetch horoscope data. Please try again later."
    except Exception as e:
        return None, str(e)

@app.route("/", methods=["GET", "POST"])
def index():
    horoscope = {}
    error = None
    zodiac_sign = ""
    time_period = ""

    if request.method == "POST":
        zodiac_sign = request.form.get("zodiac_sign", "").lower()
        time_period = request.form.get("time_period", "").lower()

        # Validate user input
        if zodiac_sign not in VALID_ZODIAC_SIGNS:
            error = "Invalid zodiac sign. Please select a valid sign."
        elif time_period not in VALID_TIME_PERIODS:
            error = "Invalid time period. Please select 'today', 'yesterday', or 'tomorrow'."
        else:
            # Fetch horoscope data
            horoscope, api_error = fetch_horoscope(zodiac_sign, time_period)
            if api_error:
                error = api_error

    return render_template(
        "index.html",
        horoscope=horoscope,
        error=error,
        zodiac_sign=zodiac_sign,
        time_period=time_period,
        valid_zodiac_signs=VALID_ZODIAC_SIGNS,
        valid_time_periods=VALID_TIME_PERIODS
    )

if __name__ == "__main__":
    app.run(debug=True)