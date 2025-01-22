from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Function to fetch horoscope
def get_horoscope(sign):
    url = "https://aztro.sameerkumar.website/"
    params = {
        "sign": sign,
        "day": "today"
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["description"]
    else:
        return "Unable to fetch horoscope."

# Homepage route
@app.route("/", methods=["GET", "POST"])
def home():
    horoscope = None
    if request.method == "POST":
        zodiac_sign = request.form.get("zodiac_sign")
        horoscope = get_horoscope(zodiac_sign)
    return render_template("index.html", horoscope=horoscope)

if __name__ == "__main__":
    app.run(debug=True)