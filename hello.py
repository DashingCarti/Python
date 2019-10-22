from darksky import forecast
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = "Homepage"
    weather = forecast.currently.summary
    return render_template("index.html", title=title, weather=weather)


@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)


@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)


if __name__ == "_main_":
    app.run(debug=True)

# API

from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

API_KEY = 'e88815cf4a9aa3410a6813d892740eda'

# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 28.572138
longitude = 77.259650
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False,  # default `False`
    lang=languages.ENGLISH,  # default `ENGLISH`
    units=units.AUTO,  # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS]  # default `[]`
)

# Final wrapper identical for both ways
forecast.latitude  # 42.3601
forecast.longitude  # -71.0589
forecast.timezone  # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently  # CurrentlyForecast. Can be found at darksky/forecast.py
forecast.minutely  # MinutelyForecast. Can be found at darksky/forecast.py
forecast.hourly  # HourlyForecast. Can be found at darksky/forecast.py
forecast.daily  # DailyForecast. Can be found at darksky/forecast.py
forecast.alerts  # [Alert]. Can be found at darksky/forecast.py
