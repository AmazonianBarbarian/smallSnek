import requests

baseUrl = 'https://api.weather.gov/gridpoints/TSA/107,100/forecast/hourly' # Fayetteville, AR forcast
response = requests.get(baseUrl)
forecast = response.json()

print(str(forecast['properties']['periods'][0]['temperature']) + " degrees F")