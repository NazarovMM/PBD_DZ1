#036BF2C7B7FB286B746A0158DC484676
import requests
import json
from pathlib import Path

api_key = "036BF2C7B7FB286B746A0158DC484676"
steam_id = "76561198028121353"
game_info = []
start_index = 21001
end_index = 0
counter = 0

print('Нач индекс ', start_index)
print('Кон индекс ', end_index)

games_file_path = Path('games.json')
if games_file_path.is_file():
    with open(games_file_path, 'r') as json_file:
        games = json.load(json_file)
else:
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&include_appinfo=1&include_played_free_games=1&format=json"
    response = requests.get(url)
    games = [game['appid'] for game in response.json()['response']['games']]
    with open(games_file_path, 'w') as json_file:
        json.dump(games, json_file)

json_file_path = Path('game_info.json')
if json_file_path.is_file():
    with open(json_file_path, 'r') as json_file:
        game_info = json.load(json_file)


# for game_id in range(start_game_id, end_game_id):
#     url = f"http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={api_key}&appid={game_id}"
#     response = requests.get(url)
#     current_json = response.json()
#     if current_json and current_json.get('game'):
#         game_info.append(current_json)

for game_id in games[start_index:]:
    counter+=1
    print(counter, ' : \t', game_id)
    url = f"http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={api_key}&appid={game_id}"
    response = requests.get(url)
    current_json = response.json()
    if current_json and current_json.get('game'):
        game_info.append(current_json)

with open(json_file_path, 'w') as json_file:
    json.dump(game_info, json_file)