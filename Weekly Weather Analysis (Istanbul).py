import requests

def analyze_weather(temps):
    print("--- Istanbul Weekly Weather ---")
    
    max_t = max(temps)
    min_t = min(temps)
    avg_t = sum(temps) / len(temps)
    
    print(f"Max: {max_t}°C | Min: {min_t}°C | Avg: {avg_t:.2f}°C\n")
    
    # checking daily conditions
    for i, temp in enumerate(temps):
        day = i + 1 
        
        # New temperature logic
        if temp > 20:
            print(f"Day {day} ({temp}°C) -> Hot")
        elif 10 <= temp <= 20:
            print(f"Day {day} ({temp}°C) -> Normal")
        else:
            print(f"Day {day} ({temp}°C) -> Cold")

def fetch_weather_data():
    # Istanbul coordinates
    lat = 41.01
    lon = 28.95
    
    # dynamically building the url
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=auto"
    
    try:
        res = requests.get(url)
        data = res.json()
        return data["daily"]["temperature_2m_max"]
    except Exception as e:
        print("API connection failed:", e)
        return []

if __name__ == "__main__":
    live_data = fetch_weather_data()
    
    if live_data:
        analyze_weather(live_data)
