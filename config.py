from dotenv import dotenv_values

MIEM_TOKEN = dotenv_values(".env").get('MIEM_TOKEN')
LICHESS_TOKEN = dotenv_values(".env").get('LICHESS_TOKEN')
LICHESS_NICK = dotenv_values(".env").get('LICHESS_NICK')
