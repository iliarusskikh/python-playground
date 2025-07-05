#ea417832cfe8d082b203c2cf821ddd29
#pip install -r requirements.txt
from typing import Any
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import requests
import os
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Access the variables


mcp = FastMCP("weather",dependencies=["requests"])

@mcp.tool()
def get_weather(city: str) -> dict[str, Any]:
    """ Get current weather for a location"""
    
    api_key = os.getenv('API_KEY')
    #gets the location from a city
    geo_url = (f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}")
    geo_data = requests.get(geo_url).json()
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']
    
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_data = requests.get(weather_url).json()
    
    return {
        "location": city,
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["main"],
    }




if __name__ == "__main__":
    mcp.run()
