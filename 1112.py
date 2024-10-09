import requests

url = "https://www.sofascore.com/api/v1/unique-tournament/17/season/61627/standings/total"

# querystring = {"page":"2"}

# headers = {
# 	"x-rapidapi-key": "2daa2e230amsh7532dc983ab54eap1308f9jsn6eb5edb6308f",
# 	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
# }

response = requests.get(url)
data = response.json()['standings']

# for d in data:
# 	for i in d['rows']:
# 		print(f"{type(i['position'])} - {i['team']['name']}")


def get_table():
	tournament_table: str = ''
	for d in data:
		for i in d['rows']:
			tournament_table += (f"{str(i['position'])} - {i['team']['name']}\n")

	return tournament_table

print(get_table())