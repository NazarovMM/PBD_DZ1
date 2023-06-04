import psycopg2
import json

# параметры подключения к БД
conn_params = {
    "host": "localhost",
    "database": "dz",
    "user": "postgres",
    "password": "password"
}

# имя файла с данными
filename = "game_info.json3.json"

# подключаемся к БД
conn = psycopg2.connect(**conn_params)

# открываем файл с данными и загружаем их в список
with open(filename, "r") as f:
    data = json.load(f)

# создаем курсор для выполнения запросов
cur = conn.cursor()

# создаем таблицу для хранения данных, если её еще нет
cur.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id SERIAL PRIMARY KEY,
        game_name TEXT,
        game_version TEXT,
        available_game_stats JSONB
    )
""")

# добавляем данные в таблицу
for item in data:
    game = item["game"]
    cur.execute("""
        INSERT INTO games (game_name, game_version, available_game_stats)
        VALUES (%s, %s, %s)
    """, (game["gameName"], game["gameVersion"], json.dumps(game["availableGameStats"])))

# сохраняем изменения и закрываем соединение
conn.commit()
cur.close()
conn.close()
