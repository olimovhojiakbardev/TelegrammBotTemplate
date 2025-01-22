from bot.dispatchers import dp
from bot.handlers.main import main


dp.include_router(*[
    main
])