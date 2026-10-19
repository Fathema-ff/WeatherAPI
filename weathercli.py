import json
import os
import click
import requests 
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API = os.getenv("API_key")
class tool:
    def __init__(self, city):
        self.city = city
        if not API:
            raise click.UsageError(
                "Missing API key"
            )

        
    def weather(self, city):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={API}&units=metric")
            data = response.json()
            return {
                "City": self.city,
                "Temperature": data["main"]["temp"],
                "Time": datetime.now().strftime("%d/%m/%Y,%H:%M:%S"),
            } 
            
        except Exception as e:
            return "Error"

@click.command()
@click.argument("city")
def cli(city):
    api = tool(city)
    responsecli = api.weather(city)
    click.echo(f"""Weather in {responsecli["City"]} at {responsecli["Time"]} is {responsecli["Temperature"]} C""")
if __name__ == "__main__":
    cli()