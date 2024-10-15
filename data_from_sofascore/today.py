import datetime

import requests


def today_list():
    today = str(datetime.date.today())
    url = f"https://www.sofascore.com/api/v1/sport/football/scheduled-events/{today}"
    table: str = ''
    response = requests.get(url).json()['events']
    for d in response:
        if 'uefa nations league' in d['tournament']['name'].lower():
            table += f"{str(datetime.datetime.fromtimestamp(d['startTimestamp']).time())[: -3]} {d['homeTeam']['name']} {d['awayTeam']['name']}\n "
    return table
