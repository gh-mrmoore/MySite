import requests

#get the weather from open-weather-map
def my_weather():
    api_address = "http://api.openweathermap.org/data/2.5/weather?zip=66062,us&units=imperial&APPID="
    api_code = "2d4cdcba967ce53aae8c4db47fd6b052"
    url = api_address + api_code

    json_data = requests.get(url).json()

    current_weather = json_data['weather'][0]['main']

    icon_code = json_data['weather'][0]['icon']

    icon_url = "http://openweathermap.org/img/w/" + icon_code + ".png"

    current_temp = json_data['main']['temp']

    weather_tuple = (current_weather, icon_url, current_temp)

    return weather_tuple

def main():
    print("You ran the main function.")

if __name__ == "__main__":
    main()