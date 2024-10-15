import datetime

import requests


# querystring = {"page":"2"}

# headers = {
# 	"x-rapidapi-key": "2daa2e230amsh7532dc983ab54eap1308f9jsn6eb5edb6308f",
# 	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
# }
def today_list():
	today = str(datetime.date.today())
	url = f"https://www.sofascore.com/api/v1/sport/football/scheduled-events/{today}"
	table: str = ''
	response = requests.get(url).json()['events']
	for d in response:
		if 'uefa nations league' in d['tournament']['name'].lower():
			table += f"{str(datetime.datetime.fromtimestamp(d['startTimestamp']).time())[: -3]} {d['homeTeam']['name']} {d['awayTeam']['name']}\n "
	return table
print(online_list())