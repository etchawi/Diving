Weather and Sea Condition Data Retrieval Script
Overview
This Python script retrieves and displays current weather and sea condition data using two external APIs:

OpenWeatherMap API – Provides weather data such as temperature, pressure, humidity, and wind speed.
StormGlass API – Provides sea condition data such as wave height, sea level, swell direction, and water temperature.
Requirements
Python 3.12 or higher
requests library
arrow library
OpenWeatherMap and StormGlass API keys
Setup
Obtain API keys from OpenWeatherMap and StormGlass.
Add the API keys and target coordinates (latitude and longitude) in the script.
Usage
Get Weather Data
The get_weather function retrieves and displays:

Current temperature (Fahrenheit)
Minimum temperature (Fahrenheit)
Pressure (hPa)
Humidity (%)
Sea level (meters)
Visibility (meters)
Wind speed (m/s)
Rain volume (mm)
Get Sea Condition Data
The sea_weather function retrieves and displays:

Wave height (feet)
Ice cover (%)
Sea level (feet)
Swell direction (degrees)
Swell height (feet)
Swell period (seconds)
Water temperature (Fahrenheit)
Wind wave height and period
Wind speed (m/s)
Conversion Details
Temperature from Kelvin to Fahrenheit:
𝐹
=
(
𝐾
×
1.8
)
−
459.67
F=(K×1.8)−459.67
Height from meters to feet:
𝑓
𝑡
=
𝑚
×
3.281
ft=m×3.281
Water temperature from Celsius to Fahrenheit:
𝐹
=
(
𝐶
×
9
/
5
)
+
32
F=(C×9/5)+32
Output
The script outputs weather and sea condition data to the console. Missing values are handled with a default of 'N/A'.

Notes
Ensure API keys are active and not rate-limited.
StormGlass API provides data in UTC time.
The script handles missing values gracefully.
