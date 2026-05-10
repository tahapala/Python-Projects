import requests  # This library allows us to pull data from the internet

def analyze_weather(weekly_temps):
    print("--- Weekly Weather Analysis (Istanbul) ---")
    
    highest_temp = max(weekly_temps)
    lowest_temp = min(weekly_temps)
    
    print(f"Highest Temperature: {highest_temp}°C")
    print(f"Lowest Temperature: {lowest_temp}°C")
    
    average_temp = sum(weekly_temps) / len(weekly_temps)
    print(f"Average Temperature: {average_temp:.2f}°C")
    
    print("\n--- Daily Status and Warnings ---")
    
    for i in range(len(weekly_temps)):
        current_temp = weekly_temps[i]
        day_number = i + 1 
        
        if current_temp < 10:
            print(f"Day {day_number} ({current_temp}°C): WARNING - Frost danger! It is very cold.")
        elif current_temp >= 30:
            print(f"Day {day_number} ({current_temp}°C): WARNING - Heatwave! Remember to stay hydrated.")
        else:
            print(f"Day {day_number} ({current_temp}°C): The weather is optimal.")

def get_istanbul_weather():
    print("Fetching live weather data for Istanbul from API...")
    
    # Istanbul coordinates: Latitude (Enlem) 41.01, Longitude (Boylam) 28.95
    # We are asking the API for the daily maximum temperatures for the next 7 days
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=41.0138&longitude=28.9497&daily=temperature_2m_max&timezone=auto"
    
    # Send a GET request to the URL
    response = requests.get(api_url)
    
    # Convert the incoming data to JSON (Python Dictionary format)
    data = response.json()
    
    # Extract just the array of temperatures from the complex JSON data
    # The API returns it under 'daily' -> 'temperature_2m_max'
    temperatures_array = data["daily"]["temperature_2m_max"]
    
    return temperatures_array

# --- Program Execution Section ---

# 1. Pull the real data using our API function
live_temperatures = get_istanbul_weather()

print("\nIncoming Data Array:", live_temperatures)
print("-" * 40)

# 2. Send the real data to our analysis function
analyze_weather(live_temperatures)