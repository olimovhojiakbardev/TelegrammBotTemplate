from os import getenv

from dotenv import load_dotenv
from utils.settings import ENV_PATH
load_dotenv(ENV_PATH)

class BotConfig:
    TOKEN = getenv("BOT_TOKEN")

class DBConfig:
    DB_NAME = getenv("DB_NAME")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_PORT = getenv("DB_PORT")
    DB_HOST = getenv("DB_HOST")

class WebConfig:
    pass

class Config:
    bot = BotConfig()
    db = DBConfig()
    web = WebConfig()