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

ID_SPOTIFY = dotenv_values(".env").get('ID_SPOTIFY')
if ID_SPOTIFY is None:
    ID_SPOTIFY = os.getenv('ID_SPOTIFY')

X_RapidAPI_Key = dotenv_values(".env").get('X_RapidAPI_Key')
if X_RapidAPI_Key is None:
    X_RapidAPI_Key = os.getenv('X_RapidAPI_Key')

X_RapidAPI_Host = dotenv_values(".env").get('X_RapidAPI_Host')
if X_RapidAPI_Host is None:
    X_RapidAPI_Host = os.getenv('X_RapidAPI_Host')


