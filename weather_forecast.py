import urequests
import utilities.config as config

def kelvin_to_celsius(value):
    return round(value-273.15,1)


        
def get_weather_forecast():
    # Build the request to the API
    response = urequests.get(config.WEATHER_URL + config.CITY + "&appid=" + config.WEATHER_API)
    # Convert to a JSON object
    response_data = response.json()
    
    weater_forecast = {"current_temperature":kelvin_to_celsius(response_data["main"]["temp"]),
                       "max_temperature": kelvin_to_celsius(response_data["main"]["temp_max"]),
                       "min_temperature": kelvin_to_celsius(response_data["main"]["temp_min"]),
                       "feels_like":kelvin_to_celsius(response_data["main"]["feels_like"]),
                       "humidity": response_data["main"]["humidity"],
                       "pressure": response_data["main"]["pressure"],
                       "main_forecast":response_data["weather"][0]["main"],
                       "description_forecast":response_data["weather"][0]["description"],
                       "icon":response_data["weather"][0]["icon"],
                       "wind_speed":response_data["wind"]["speed"],
                       "wind_direction":response_data["wind"]["deg"]
                    }

    return weater_forecast