#ea417832cfe8d082b203c2cf821ddd29
#uv add "mcp[cli]"
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



class CoinInfoResponse(BaseModel):
    name: str
    symbol: str
    current_price: float
    market_cap: float
    total_volume: float
    price_change_24h: float



def get_crypto_info(cryptocurrency: str) -> CoinInfoResponse:
    coin_id =""
    match cryptocurrency.lower():
        case "ethereum"|"eth"|"ethereum network"|"ethereum blockchain":
            coin_id = "ethereum"
        case "base"| "base network"|"base blockchain":
            coin_id = "ethereum"
        case "solana"|"sol"|"solana blockchain"|"solana network":
            coin_id = "solana"
        case "bsc"|"Bsc"| "bsc network"|"bnb"|"bsc blockchain":
            coin_id = "binancecoin"
        case "polygon"|"matic-network"|"matic"|"pol"|"polygon blockchain":
            coin_id = "matic-network"
        case "avalanche"|"avalanche blockchain":
            coin_id = "avalanche-2"
        case "arbitrum"|"arbitrum network"|"arb"|"arbitrum blockchain":
            coin_id = "arbitrum"
        case "optimism"|"optimism network"|"op"|"optimism blockchain":
            coin_id = "optimism"
        case "sui"|"sui blockchain":
            coin_id = "sui"
        case "ronin"|"ronin blockchain":
            coin_id = "ronin"
        case "bitcoin"|"btc"|"bitcoin blockchain":
            coin_id = "bitcoin"
        case _:
            return ValueError(f"Unsupported cryptocurrency: {cryptocurrency}. Please, input the name of the supported crypto.")  # Handle unexpected inputs
            #raise

    """Fetch cryptocurrency information from CoinGecko API"""
    
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    
    try:
        response = requests.get(url)
        print(f"🚀 URL for {coin_id} received...")
        response.raise_for_status()  # Raises an error for non-200 responses

        data = response.json()
        
        return CoinInfoResponse(
            name=data['name'],
            symbol=data['symbol'].upper(),
            current_price=data['market_data']['current_price']['usd'],
            market_cap=data['market_data']['market_cap']['usd'],
            total_volume=data['market_data']['total_volume']['usd'],
            price_change_24h=data['market_data']['price_change_percentage_24h']
        )
    
    except requests.exceptions.RequestException as e:
        agent._logger.error(f"⚠️ API Request Failed: {e}")
        return CoinInfoResponse(
            name="Unknown",
            symbol="N/A",
            current_price=0.0,
            market_cap=0.0,
            total_volume=0.0,
            price_change_24h=0.0
        )



@mcp.tool()
async def get_crypto(cryptocurrency: str) -> CoinInfoResponse:#(str)CoinInfoResponse
    """Get information for a selected cryptocurrency"""
    
    print(f"Received:{cryptocurrency}.")
    crypto_data = get_crypto_info(cryptocurrency) #to be tested
    #crypto_data = f"(name='{cryptocurrency}', symbol='{cryptocurrency}', current_price=12345.0, market_cap=678.0, total_volume=9.0, price_change_24h=10.0)"
    
    if ("Unknown" or None) in str(crypto_data):
        return "Unable to fetch information for a selected cryptocurrency."
    
    #return "\n---\n".join(str(crypto_data))
    return crypto_data


#def main():
    #print(f"Hello from mcp1!{api_key}")

if __name__ == "__main__":
    mcp.run()


#mcp dev src/mcp_weather.py

#{
#    "mcpServers": {
#        "weather": {
#            "command": "uv",
#            "args": ["run", "[...]","/path/to/ur/project/mcp_weather.py",
#            "env": {
#                "API_KEY": "your_api_key"
#             }
#        }
#    }
#
#}
