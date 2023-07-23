import json
import requests

def get_weather(city):
    link = 'http://api.openweathermap.org/data/2.5/find?q='+city+'&type=like&APPID=ea709dc15dae1781542fcc4aa1239794'
    weather = json.loads(requests.get(link).text)   # Команду преобразования строки в словарь нашел в интернете
    print(requests.get(link).text)  # Хоть решение наверное могло быть и лучше зато сделал полносью сам
    print(f'Weather in {city}:')
    if weather['list'][0]['rain'] != None:
        print(f"Rain - {weather['list'][0]['rain']}")
    if weather['list'][0]['snow'] != None:
        print(f"Snow - {weather['list'][0]['snow']}")
    print(f"Temperature: {int(weather['list'][0]['main']['temp'] - 270)} C")
    print(f"Pressure: {weather['list'][0]['main']['pressure']}")
    print(f"Humidity: {weather['list'][0]['main']['humidity']}%")


def get_joke():
    link = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'
    joke = json.loads(requests.get(link).text)
    print('Joke:')
    print(joke["setup"])
    print(joke["delivery"])


# get_weather('Tashkent')
# get_joke()