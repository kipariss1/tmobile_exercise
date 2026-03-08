import os
from pyowm import OWM
from pyowm.utils.config import get_default_config

# Get environment variables
api_key = os.getenv('OWM_API_KEY')
city = os.getenv('OWM_CITY')

if not api_key or not city:
    print("Please set OWM_API_KEY and OWM_CITY environment variables.")
    exit(1)

# Set language and units
config_dict = get_default_config()
config_dict['language'] = 'en'
config_dict['units'] = 'metric'  # Celsius (SI units)

# Initialize OWM
owm = OWM(api_key, config_dict)
mgr = owm.weather_manager()

# Get current weather
observation = mgr.weather_at_place(city)
weather = observation.weather

# Print formatted output
print(f'city="{city}", description="{weather.detailed_status}", temp={weather.temperature("celsius")["temp"]}, humidity={weather.humidity}')