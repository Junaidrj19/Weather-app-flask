from flask import Flask, render_template, request
import requests

API_KEY = "43cdf19a12b2e432f93d88bfbac4abd3"
Base_url = "https://api.openweathermap.org/data/2.5/weather"


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def get_weather():
    city = None
    weather_data = None
    error = None
    params = None

    if request.method == 'POST':
        city = request.form.get('city')

        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric',
            }

            response = requests.get(Base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': city.title(),
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description'],
                    'wind_speed': data['wind']['speed'],
                }
            else:
                return "City not found", 404

    return render_template("weather.html", weather_data=weather_data,error=error)

if __name__ == '__main__':
    app.run(debug=True)