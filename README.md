# 🌤️ Flask Weather App

A sleek, lightweight Weather Application built with Flask that fetches real-time data using the OpenWeather API.

This project demonstrates how to build a functional backend that consumes third-party APIs, handles JSON data, and renders dynamic content using Jinja2 templates.

---

## 🚀 Features

- **Real-time Search:** Get instant weather data by city name.
- **Detailed Metrics:** Displays temperature (°C), weather conditions, humidity, and wind speed.
- **Modern UI:** Clean interface featuring glassmorphism CSS styling.
- **Error Handling:** Graceful alerts for invalid city names or API connection issues.

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **API:** [OpenWeatherMap API](https://openweathermap.org/api)
- **Frontend:** HTML5, CSS3 (Jinja2 Templates)
- **HTTP Client:** `requests` library

---

## 📁 Project Structure

weather_app/
├── static/
│ └── css/
│ └── style.css
├── templates/
│ ├── base.html
│ └── weather.html
├── app.py
├── requirements.txt
└── README.md

⚙️ Setup & Installation

1. Clone the repository
   Bash

git clone https://github.com/Junaidrj19/Weather-app-flask
cd weather_app

2. Create a virtual environment
   Bash

# Windows

python -m venv venv
venv\Scripts\activate

# macOS/Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
   Bash
   pip install -r requirements.txt

4. Configuration
   Create a file named .env or edit app.py to include your OpenWeather API Key:

Python
API_KEY = "your_api_key_here"

5. Run the Application
   Bash

python app.py
Visit http://127.0.0.1:5000 in your browser.

📌 Learning Outcomes

API Integration: Learned to parse documentation and use parameters for GET requests.

JSON Manipulation: Extracted nested data from complex JSON structures.

State Management: Handled user input and displayed conditional responses based on API success/failure.

Project Architecture: Followed Flask best practices for directory organization.

🔮 Future Improvements
[ ] Add dynamic weather icons based on conditions (Sunny, Rainy, etc.).

[ ] Implement a toggle for Celsius/Fahrenheit.

[ ] Add "Geolocation" to fetch weather for the user's current city automatically.

[ ] Deploy the app to Heroku or PythonAnywhere.

🤝 Acknowledgements

OpenWeather API
Flask Documentation
