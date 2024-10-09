import requests

url = "https://www.sofascore.com/api/v1/sport/football/events/live"

# querystring = {"page":"2"}

# headers = {
# 	"x-rapidapi-key": "2daa2e230amsh7532dc983ab54eap1308f9jsn6eb5edb6308f",
# 	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
# }

response = requests.get(url)
data = response.json()['events']


for d in data:
	if int(d['homeScore']['current']) + int(d['awayScore']['current']) >= 2:
		print(f"{d['tournament']['name']}\n{d['homeTeam']['name']} vc {d['awayTeam']['name']}\n {d['homeScore']['current']} ------------{d['awayScore']['current']}")



