# Weather Dashboard for Store Planning

## 📌 Project Overview
Store managers need quick weather insights for scheduling staff.  
This project fetches **daily weather data** for the **top 5 store cities** using the OpenWeatherMap API and stores it in a clean CSV report.

---

## 🎯 Business Requirement
- Provide **daily weather conditions** for 5 cities.  
- Help store managers **adjust staff schedules** based on weather.  

---

## ✅ Acceptance Criteria
- Output file named: `weather_report_YYYYMMDD.csv`  
- Exactly **5 rows** (one per city).  
- All temperatures in **Celsius**.  
- Columns:
  - `City Name`
  - `Temperature (°C)`
  - `Weather Condition`
  - `Date of Extraction` (IST timestamp)

---

## 🛠 Tech Stack
- **Python 3.10+**  
- **Libraries**: `requests`, `pandas`, `python-dotenv`, `tzdata`  
- **Data Source**: [OpenWeatherMap Current Weather API](https://openweathermap.org/current)

---

## 📂 Project Structure
weather_dashboard/
├─ .env.example
├─ cities.txt
├─ requirements.txt
├─ src/
│  ├─ __init__.py
│  ├─ config.py
│  ├─ utils.py
│  ├─ weather_client.py
│  ├─ transform.py
│  ├─ storage.py
│  └─ main.py
└─ tests/
   ├─ test_transform.py
   └─ test_integration.py

