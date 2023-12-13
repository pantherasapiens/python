import requests
from datetime import datetime, timedelta

# API endpoint URL
url = "https://api.open-meteo.com/v1/forecast"

# Coordinates for latitude and longitude (replace with your desired location)
latitude = 25.5941
longitude = 85.1356

# Query parameters
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m"
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Access the hourly temperature data (a list of float values)
    hourly_temperatures = data.get("hourly", {}).get("temperature_2m", [])
    
    # Get the current time
    current_time = datetime.now()
    
    # Display the hourly temperature data with generated timestamps
    print("Hourly Temperature Data (2m above ground):")
    for index, temperature in enumerate(hourly_temperatures, 1):
        # Generate timestamps based on the current time and index
        timestamp = current_time + timedelta(hours=index)
        timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"{timestamp_str}: {temperature}°C")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
