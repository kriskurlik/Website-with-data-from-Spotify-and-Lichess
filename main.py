"""
created by Goncharova Kristina BIV221
Get information about person from Cabinet MIEM, Lichess, Spotify.
"""
import json
import requests
import berserk
from jinja2 import Template
import config

# Данные из кабинета МИЭМа
response = requests.get('https://cabinet.miem.hse.ru/api/student_profile',
                        headers={"x-auth-token": config.MIEM_TOKEN},
                        timeout=10)
r = response.json()
with open("./MIEM.json", 'w', encoding='utf-8') as fl:
    fl.write(json.dumps(r, ensure_ascii=False))

# Данные из Lichess
session = berserk.TokenSession(config.LICHESS_TOKEN)
client = berserk.Client(session=session)
a = client.users.get_public_data(config.LICHESS_NICK)
with open("./Lichess.json", "w", encoding="utf-8") as fl1:
    fl1.write(str(client.users.get_public_data(config.LICHESS_NICK)))

# Данные из Спотифая
URL = "https://spotify23.p.rapidapi.com/user_profile/"
querystring = {"id": str(config.ID_SPOTIFY), "playlistLimit": "10",
               "artistLimit": "10"}
headers = {
    "X-RapidAPI-Key": str(config.X_RapidAPI_Key),
    "X-RapidAPI-Host": str(config.X_RapidAPI_Host)
}
answer = requests.request("GET", URL, headers=headers, params=querystring,
                          timeout=10)
with open("./Spotify.json", "w", encoding="utf-8") as fl2:
    fl2.write(answer.text)


TEMPLATE_PATH = "index1.html"
INDEX_PATH = "index.html"


def create_template(template_path):
    """
    Функция формирует шаблон из файла
    :param template_path:
    :return: Template(template_html)
    """
    with open(template_path, "r", encoding='utf-8') as fl4:
        template_html = fl4.read()
        return Template(template_html)


def get_name_of_playlist(ans):
    """
    Функция заполняет массив назаниями плейлистов
    :param ans:
    :return: names
    """
    names = []
    for i in range(0, ans.json()["total_public_playlists_count"]):
        names.append(ans.json()["public_playlists"][i]["name"])
    return names


if __name__ == '__main__':
    template = create_template(TEMPLATE_PATH)
    print(a)
    playlist = get_name_of_playlist(answer)
    rendered_page = template.render(
        name=r["data"][0]["main"]["name"],
        status=r["data"][0]["main"]["description"][0],
        email=r["data"][0]["main"]["email"],
        chatlink=r["data"][0]["main"]["chatLink"],
        avatar=r["data"][0]["main"]["pic"],
        nick_name=answer.json()["name"],
        following_count=answer.json()["following_count"],
        playlist_names=playlist,
        name_li=a["username"],
        url_li=a["url"],
        all_games=a["count"]["all"],
        win=a["count"]["win"],
        loss=a["count"]["loss"]


    )
    with open(INDEX_PATH, "w", encoding='utf-8') as fl3:
        fl3.write(rendered_page)
