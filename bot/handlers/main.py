from string import ascii_uppercase
from aiogram.types import Message
from aiogram import Router, html
from aiogram.filters import CommandStart

main = Router()

@main.message(CommandStart())
async def start(message:Message):
    await message.answer(f"Hello, {html.bold(message.from_user.first_name)}!")
