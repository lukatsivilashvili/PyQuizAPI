import requests
import json
import sqlite3

url = 'https://animechan.vercel.app/api/random'


def print_anime_quotes(api_url):
    r = requests.get(api_url)
    print(r.status_code)
    print(r.headers, "\n")

    result = r.text
    result_json = json.loads(result)
    result_struct = json.dumps(result_json)
    print(result_struct)


def return_anime_quotes(api_url):
    r = requests.get(api_url)
    result = r.text
    result_json = json.loads(result)
    return result_json


# ბაზაში ინახავს აპი-ს მიერ დაბრუნებულ ანიმეს სახელს, პერსონაჟს და მის გამონათქვამს

def create_and_insert_in_db():
    conn = sqlite3.connect("aniQuotes.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS quotes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                anime VARCHAR (50),
                character VARCHAR (50),
                quote VARCHAR (100)
                )''')

    dict = return_anime_quotes(url)
    anime = dict['anime']
    character = dict['character']
    quote = dict['quote']
    cursor.execute("INSERT INTO quotes (anime, character, quote) VALUES (?, ?, ?)", (anime, character, quote))
    conn.commit()
    conn.close()


create_and_insert_in_db()
print_anime_quotes(url)
