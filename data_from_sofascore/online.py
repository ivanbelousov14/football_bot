import requests
from datetime import datetime

def online_list():
    url = "https://www.sofascore.com/api/v1/sport/football/events/live"
    table: str = ''
    response = requests.get(url).json()['events']
    # add id leagues
    for d in response:
        table += f"{d['tournament']['name']}\n {datetime.fromtimestamp(d['startTimestamp']).time()} <b>{d['homeTeam']['name']} {d['homeScore']['current']} - {d['homeScore']['current']} {d['awayTeam']['name']}</b> "
    return table


def send_mess():
    return "123"


