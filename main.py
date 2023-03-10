import requests
import config
import json
import berserk
# Данные из кабинета МИЭМа
fl = open('./MIEM.json', 'w', encoding='utf-8')
response = requests.get('https://cabinet.miem.hse.ru/api/student_profile', headers={"x-auth-token": config.MIEM_TOKEN})
r = response.json()
fl.write(json.dumps(r, ensure_ascii=False))
fl.close()

# Данные из Lichess
session = berserk.TokenSession(config.LICHESS_TOKEN)
client = berserk.Client(session=session)
with open("./Lichess.json", "w", encoding="utf-8") as fl1:
    fl1.write(str(client.users.get_public_data(config.LICHESS_NICK)))
