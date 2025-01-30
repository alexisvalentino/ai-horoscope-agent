import requests

# Define the endpoint URL
url = "https://horoscope-api2.p.rapidapi.com/daily"

# Define the headers with the API key
headers = {
    "X-RapidAPI-Key": "f6c2354df6msh801d068f3b189b1p1b37cejsn1d5569b97d86",
    "X-RapidAPI-Host": "horoscope-api2.p.rapidapi.com"
}

# Define the query parameters
params = {
    "sign": "aries",
    "day": "today"
}

# Make the request
response = requests.get(url, headers=headers, params=params)

# Check the response
if response.status_code == 200:
    data = response.json()
    print("API Response:")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")