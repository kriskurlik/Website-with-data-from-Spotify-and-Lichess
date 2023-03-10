import os
from dotenv import dotenv_values

MIEM_TOKEN = dotenv_values(".env").get('MIEM_TOKEN')
if MIEM_TOKEN is None:
    MIEM_TOKEN = os.getenv('MIEM_TOKEN')

LICHESS_TOKEN = dotenv_values(".env").get('LICHESS_TOKEN')
if LICHESS_TOKEN is None:
    LICHESS_TOKEN = os.getenv('LICHESS_TOKEN')

LICHESS_NICK = dotenv_values(".env").get('LICHESS_NICK')
if LICHESS_NICK is None:
    LICHESS_NICK = os.getenv('LICHESS_NICK')
