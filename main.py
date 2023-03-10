"""
created by Goncharova Kristina BIV221
Get information about person from Cabinet MIEM and Lichess
"""
import json
import requests
import berserk
import config
# Данные из кабинета МИЭМа
with open("./MIEM.json", 'w', encoding='utf-8') as fl:
    response = requests.get('https://cabinet.miem.hse.ru/api/student_profile',
                            headers={"x-auth-token": config.MIEM_TOKEN},
                            timeout=10)
    r = response.json()
    fl.write(json.dumps(r, ensure_ascii=False))

# Данные из Lichess
session = berserk.TokenSession(config.LICHESS_TOKEN)
client = berserk.Client(session=session)
with open("./Lichess.json", "w", encoding="utf-8") as fl1:
    fl1.write(str(client.users.get_public_data(config.LICHESS_NICK)))
