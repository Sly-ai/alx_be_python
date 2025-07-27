import requests

# This code fetches the current temperature for a specific location using the Open Meteo API.
# The location is specified by latitude and longitude.
print("importing requests module...")
print()
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=9&longitude=39.5&hourly=temperature_2m,wind_speed_10m")
data = response.json()
print("Weather data fetched successfully.")

# Extract wind speed unit
wind_speed_unit = data.get("hourly_units", {}).get("wind_speed_10m")
print("Wind speed unit:", wind_speed_unit)

# Extract wind speed values for the day
wind_speeds = data.get("hourly", {}).get("wind_speed_10m", [])
print("Wind speed values for the day:", wind_speeds)

