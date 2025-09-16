import os
import requests
from dotenv import load_dotenv

# Step 1: Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise RuntimeError("❌ No API key found. Did you set OPENWEATHER_API_KEY in .env?")

# Step 2: Define base URL and parameters
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Delhi",       # city name
    "appid": API_KEY,   # your key
    "units": "metric"   # Celsius
}

# Step 3: Send GET request
response = requests.get(BASE_URL, params=params, timeout=10)

# Step 4: Check success or failure
if response.status_code != 200:
    print("❌ API call failed:", response.status_code, response.text)
else:
    data = response.json()
    print("✅ API call success!")
    print("Raw JSON response:")
    print(data)
