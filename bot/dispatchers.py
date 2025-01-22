from os import getenv
from aiogram import Dispatcher
from utils.env_data import Config

TOKEN = Config.bot.TOKEN
dp = Dispatcher()