import asyncio
import logging
import sys

from src.bot_factory import BotFactory
from src.core.database import DataBase


if __name__ == "__main__":
    db = DataBase()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    db.init_db()
    asyncio.run(BotFactory.start_bot())
