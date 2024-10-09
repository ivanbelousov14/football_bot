import requests
import datetime

url = "https://sofascore.p.rapidapi.com/teams/get-next-matches"

querystring = {"teamId":"38","pageIndex":"0"}

headers = {
	"x-rapidapi-key": "2daa2e230amsh7532dc983ab54eap1308f9jsn6eb5edb6308f",
	"x-rapidapi-host": "sofascore.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
list_ = response.json()['events']

for l in list_:
	print(f"{datetime.datetime.fromtimestamp(l['startTimestamp'])}\n{l['tournament']['name']}\n{l['homeTeam']['name']} --- {l['awayTeam']['name']}")