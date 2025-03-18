import requests, arrow
import openai
OPEN_WEATHER_API_KEY = "Type API"  
STORM_GLASS_API_KEY = "Type API"
lat = 27.710074
lon = -97.108435
def get_weather(OPEN_WEATHER_API_KEY, lat, lon):
  # lat: Lattide - lon: Longitude
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}"
  response = requests.get(url).json()

  temp = response['main']['temp']
  temp = (temp * 1.8) - 459.67
  temp_min = response['main']['temp_min']
  temp_min = (temp_min * 1.8) - 459.67
  pressure = response['main']['pressure']
  humidity = response['main']['humidity']
  sea_level = response['main']['sea_level']
  visibility = response['visibility']
  wind_speed = response['wind']['speed']
  rain = response.get('rain', {}).get('1h', 0) #default value 0 if no rain

  print(f"Surface Temprature {temp:.2f} F")
  print(f"Temp Min {temp_min:.2f} F")
  print(f"Pressure: {pressure} hPa")
  print(f"Humidity: {humidity}%")
  print(f"Sea Level: {sea_level} meters")
  print(f"Visibility: {visibility} meters")
  print(f"Wind Speed: {wind_speed:.2f} m/s")
  print(f"Rain Volume: {rain:.2f} mm")

get_weather( OPEN_WEATHER_API_KEY,lat ,lon)


def sea_weather(STORM_GLASS_API_KEY, lat, lon):
  current_time = arrow.now().to('UTC')
  response = requests.get('https://api.stormglass.io/v2/weather/point',
                          params={
    'lat': 58.7984,
    'lng': 17.8081,
    'params': ','.join(['waveHeight', 'iceCover', 'seaLevel','swellDirection', 'swellHeight', 'swellPeriod', 'waterTemperature','waveDirection','wavePeriod', 'windWaveDirection', 'windWaveHeight', 'windWavePeriod','windSpeed']),
    'time': current_time.timestamp()
  },
  headers={'Authorization': STORM_GLASS_API_KEY
  }
  )
  json_data = response.json()

      # Extract relevant data (taking the first available value for each parameter)
  data = json_data['hours'][0]

  wave_height_m = data.get('waveHeight', {}).get('sg', 'N/A')
  ice_cover = data.get('iceCover', {}).get('sg', 'N/A')
  sea_level_m = data.get('seaLevel', {}).get('sg', 'N/A')
  swell_direction = data.get('swellDirection', {}).get('sg', 'N/A')
  swell_height_m = data.get('swellHeight', {}).get('sg', 'N/A')
  swell_period = data.get('swellPeriod', {}).get('sg', 'N/A')
  water_temperature_c = data.get('waterTemperature', {}).get('sg', 'N/A')
  wave_direction = data.get('waveDirection', {}).get('sg', 'N/A')
  wave_period = data.get('wavePeriod', {}).get('sg', 'N/A')
  wind_wave_direction = data.get('windWaveDirection', {}).get('sg', 'N/A')
  wind_wave_height_m = data.get('windWaveHeight', {}).get('sg', 'N/A')
  wind_wave_period = data.get('windWavePeriod', {}).get('sg', 'N/A')
  wind_speed_m_s = data.get('windSpeed', {}).get('sg', 'N/A')


  wave_height_ft = wave_height_m * 3.281 if isinstance(wave_height_m, (int, float)) else 'N/A'
  sea_level_ft = sea_level_m * 3.281 if isinstance(sea_level_m, (int, float)) else 'N/A'
  swell_height_ft = swell_height_m * 3.281 if isinstance(swell_height_m, (int, float)) else 'N/A'
  wind_wave_height_ft = wind_wave_height_m * 3.281 if isinstance(wind_wave_height_m, (int, float)) else 'N/A'
  water_temperature_f = (water_temperature_c * 9/5) + 32 if isinstance(water_temperature_c, (int, float)) else 'N/A'


  print(f"Wave Height: {wave_height_ft:.2f} ft")
  print(f"Ice Cover: {ice_cover} %")
  print(f"Sea Level: {sea_level_ft:.2f} ft")
  print(f"Swell Direction: {swell_direction:.2f} degrees")
  print(f"Swell Height: {swell_height_ft:.2f} ft")
  print(f"Swell Period: {swell_period:.2f} seconds")
  print(f"Water Temperature: {water_temperature_f:.2f} F")
  print(f"Wave Direction: {wave_direction:.2f} degrees")
  print(f"Wave Period: {wave_period:.2f} seconds")
  print(f"Wind Wave Direction: {wind_wave_direction:.2f} degrees")
  print(f"Wind Wave Height: {wind_wave_height_ft:.2f} ft")
  print(f"Wind Wave Period: {wind_wave_period:.2f} seconds")
  print(f"Wind Speed: {wind_speed_m_s:.2f} m/s")
  print(f"Lattiude is {lat} ")
  print(f"Longitude is {lon}")

sea_weather(STORM_GLASS_API_KEY, lat, lon)