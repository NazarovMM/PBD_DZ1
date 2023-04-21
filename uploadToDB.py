import psycopg2
import csv

# Устанавливаем параметры подключения к базе данных
db_host = "localhost"
db_name = "database_name"
db_user = "username"
db_password = "password"

# Открываем соединение с базой данных
conn = psycopg2.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Создаем курсор для выполнения операций в базе данных
cur = conn.cursor()

# Определяем имя таблицы и имя файла CSV
table_name = "games"
csv_file = "epic games store-video games.csv"

# Создаем таблицу в базе данных
cur.execute(f"DROP TABLE IF EXISTS {table_name}")
cur.execute(f"""
    CREATE TABLE {table_name} (
        id SERIAL PRIMARY KEY,
        game_link TEXT,
        name TEXT,
        price TEXT,
        developer TEXT,
        genres TEXT[],
        features TEXT[],
        publisher TEXT,
        release_date TEXT,
        recommended_os TEXT,
        cpu TEXT,
        memory TEXT,
        gpu TEXT,
        storage TEXT,
        critics_recommend TEXT,
        opencritic_rating TEXT,
        platform TEXT,
        top_critic_average TEXT
    )
""")

# Читаем данные из CSV-файла и добавляем их в таблицу
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        game_link = row["game_link"]
        name = row["name"]
        price = row["price of game"].replace(',', '').replace('в‚№', '')  # убираем запятые и знак валюты
        developer = row["developer of game"]
        genres = row["genres of games"].split(",")
        features = row["features of game"].split(",")
        publisher = row["publisher of game"]
        release_date = row["date release"]
        recommended_os = row["recommended_os"]
        cpu = row["cpu"]
        memory = row["memory"]
        gpu = row["gpu_x"]
        storage = row["storage"]
        critics_recommend = row["Critics Recommend"]
        opencritic_rating = row["OpenCritic Rating"].replace('%', '')  # убираем знак процента
        platform = row["platform"]
        top_critic_average = row["Top Critic Average"].replace(',', '')  # убираем запятые
        cur.execute(f"""
            INSERT INTO {table_name} (
                game_link, name, price, developer, genres, features, publisher,
                release_date, recommended_os, cpu, memory, gpu, storage,
                critics_recommend, opencritic_rating, platform, top_critic_average
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            game_link, name, price, developer, genres, features, publisher,
            release_date, recommended_os, cpu, memory, gpu, storage,
            critics_recommend, opencritic_rating, platform, top_critic_average
        ))

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
cur.close()
conn.close()
