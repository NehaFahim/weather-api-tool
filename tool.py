from agents import Agent,Runner,function_tool   # type: ignore
from main import config
import os
from dotenv import load_dotenv
import requests

load_dotenv()
weather_api_key= os.getenv('WEATHER_API_KEY')

@function_tool
def get_weather(city:str) -> str:
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}")
    data = response.json()
    return f"The current weather in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."

agent = Agent(
    name="weather agent",
    instructions="you are help to assist the user to give information.",
    tools= [get_weather]
)

result = Runner.run_sync(agent,
                        'what is the current weather in Karachi today??',
                        run_config=config

)
print(result.final_output)