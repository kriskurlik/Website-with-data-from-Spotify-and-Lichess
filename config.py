import os
from dotenv import dotenv_values

Token = dotenv_values(".env").get('token')
