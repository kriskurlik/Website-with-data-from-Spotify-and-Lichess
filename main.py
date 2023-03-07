import requests
import config
import zulip

#Данные из кабинета МИЭМа
fl = open('C:/Users/user/PycharmProjects/api/GoncharovaKV.txt', 'w')
response = requests.get('https://cabinet.miem.hse.ru/api/student_profile', headers={"x-auth-token": config.cabinet_token})
r = response.json()

name = r["data"][0]["main"]["name"]
group = r["data"][0]["main"]["group"]
id = r["data"][0]["main"]["studentId"]
email = r["data"][0]["main"]["email"]
description = r["data"][0]["main"]["description"][0]
avatar = r["data"][0]["main"]["pic"]

fl.write('Данные из кабинета МИЭМа:' + '\n')
fl.write('ФИО:  ' + name + '\n')
fl.write('Группа:  ' + group + '\n')
fl.write('Статус:  ' + description + '\n')
fl.write('Почта:  ' + email + '\n')
fl.write('ID:  ' + str(id) + '\n')
fl.write('URL-аватар: ' + avatar + '\n')

fl.close()