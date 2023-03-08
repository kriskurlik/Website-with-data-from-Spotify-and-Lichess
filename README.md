# Инструкция по работе с кодом
Этот мануал поможет получить данные из ресурсов Кабинет МИЭМ и Zulip
## Как работать с кодом?
- Для получения данных из кабинета МИЭМ необходимо получить свой токен (его можно найти в консоли разработчика во вкладке Network в запросе student_profile) и скопировать его в файл .env в перемнную token без каких-либо дополнительных знаков. Запустить главную программу. Полученные данные будут отображены в формате json в файле MIEM.json
- Для получения данных из Zulip необходимо иметь при себе свой ключ Api (он находится в Личных настройках в разделе Учетная запись и конфиденциальность). Его нужно скачать, переименовать в файл api.env и перенести в директорию с файлом кода. Запустить главную программу. Полученные данные в формате json будут отображены в файле Zulip.json