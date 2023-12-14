from aiogram.types import CallbackQuery
from aiogram.filters.base import Filter


class TextFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.message.text == self.my_text
