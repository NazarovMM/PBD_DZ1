import ijson
import json

filename='game_info.json'


with open(filename, 'rb') as f:
    objects = ijson.items(f, 'item')
    buffer = []
    for index, obj in enumerate(objects):
        buffer.append(obj)
        if (index + 1) % 5000 == 0:
            with open(f'{filename}{index//5000}.json', 'w') as outfile:
                json.dump(buffer, outfile)
            buffer = []
    if buffer:
        with open(f'{filename}_{(index+1)//5000}.json', 'w') as outfile:
            json.dump(buffer, outfile)