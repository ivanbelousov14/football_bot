import requests
from prettytable import PrettyTable

about = 'Этот бот предназначен для любителей футбола. Раздел ИНФО сожержит сведения о матчах сегодня, онлайн-матчах, ' \
        'а так же турнирные таблицы чемпионтов. Раздел ИНТЕРАКТИВ предназначен для совершения виртуальных ставок'

leagues_dict: dict = {'england': 17, 'spain': 8, 'germany': 35, 'italy': 23, 'france': 34, 'russia': 203}
def epl_tournament_table():
    url = 'https://www.sofascore.com/api/v1/unique-tournament/17/season/61627/standings/total'
    data = requests.get(url).json()['standings']
    tournament_table = ''
    for i in data[0]['rows']:
        tournament_table += f"<code>{i['position']} {i['team']['name']} - {i['points']}</code> \n"

    return tournament_table

def laliga_tournament_table():
    url = 'https://www.sofascore.com/api/v1/unique-tournament/8/season/61643/standings/total'
    data = requests.get(url).json()['standings']
    tournament_table = ''
    for i in data[0]['rows']:
        tournament_table += f"<code>{i['position']} {i['team']['name']} - {i['points']}</code> \n"

    return tournament_table


def bundesliga_tournament_table():
    url = 'https://www.sofascore.com/api/v1/unique-tournament/35/season/63516/standings/total'
    data = requests.get(url).json()['standings']
    tournament_table = ''
    for i in data[0]['rows']:
        tournament_table += f"<code>{i['position']} {i['team']['name']} - {i['points']}</code> \n"

    return tournament_table


def seriea_tournament_table():
    url = 'https://www.sofascore.com/api/v1/unique-tournament/23/season/63515/standings/total'
    data = requests.get(url).json()['standings']
    tournament_table = ''
    for i in data[0]['rows']:
        tournament_table += f"<code>{i['position']} {i['team']['name']} - {i['points']}</code> \n"

    return tournament_table


def ligaone_tournament_table():
    url = 'https://www.sofascore.com/api/v1/unique-tournament/34/season/61736/standings/total'
    data = requests.get(url).json()['standings']
    tournament_table = ''
    for i in data[0]['rows']:
        tournament_table += f"<code>{i['position']} {i['team']['name']} - {i['points']}</code> \n"

    return tournament_table


def rpl_tournament_table():
    url = 'https://www.sofascore.com/api/v1/unique-tournament/203/season/61712/standings/total'
    data = requests.get(url).json()['standings']
    tournament_table = ''
    for i in data[0]['rows']:
        tournament_table += f"<code>{i['position']} {i['team']['name']} - {i['points']}</code> \n"

    return tournament_table