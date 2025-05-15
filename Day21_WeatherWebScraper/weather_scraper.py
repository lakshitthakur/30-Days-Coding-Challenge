import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"📍 Weather in {city}:")
            print(response.text)
        else:
            print("⚠️ Could not fetch weather data. Try again.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🌦️ Real-Time Weather Checker")
    city = input("Enter your city name: ")
    get_weather(city)
