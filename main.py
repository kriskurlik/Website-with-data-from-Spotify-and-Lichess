import requests
import config
import zulip
import json

# Данные из кабинета МИЭМа
fl = open('C:/Users/user/PycharmProjects/api/MIEM.json', 'w', encoding='utf-8')
response = requests.get('https://cabinet.miem.hse.ru/api/student_profile', headers={"x-auth-token": config.Token})
r = response.json()

fl.write(json.dumps(r, ensure_ascii=False))

fl.close()

# Данные из Zulip
file = open('C:/Users/user/PycharmProjects/api/Zulip.json', 'w', encoding='utf-8')

client = zulip.Client(config_file="C:/Users/user/PycharmProjects/api/api.env")
result = client.get_profile()

file.write(json.dumps(result, ensure_ascii=False))

file.close()
