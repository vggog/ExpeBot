from aiogram.fsm.state import StatesGroup, State


class AdminStates(StatesGroup):
    what_to_mailing = State()


class ButtonState(StatesGroup):
    message_with_url_button = State()


class RefUrlState(StatesGroup):
    ref_url_title = State()
