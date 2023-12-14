from aiogram.utils.keyboard import (
    InlineKeyboardButton,
    InlineKeyboardBuilder
)


def admin_menu_buttons():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Рассылка",
            callback_data="newsletter"
        ),
        InlineKeyboardButton(
            text="Взять ссылку",
            callback_data="take_link"
        ),
        InlineKeyboardButton(
            text="Статистика по доходимости",
            callback_data="profitability_statistics"
        ),
        InlineKeyboardButton(
            text="Сколько трафика",
            callback_data="how_much_traffic"
        ),
        InlineKeyboardButton(
            text="Скачать базу",
            callback_data="download_database"
        ),
    )
    builder.adjust(1)

    return builder.as_markup()


def mailing_recipient_buttons():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="По всей базе",
            callback_data="all_base"
        ),
        InlineKeyboardButton(
            text="Кто прошёл до конца",
            callback_data="who_went_to_end"
        ),
        InlineKeyboardButton(
            text="норм Чел, прошел все бонусы",
            callback_data="pick_up_all_bonus"
        ),
    )
    builder.adjust(1)

    return builder.as_markup()


def buttons_for_adding_mailing_buttons():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Добавить кнопки",
            callback_data="add_mailing_buttons"
        ),
        InlineKeyboardButton(
            text="Разослать",
            callback_data="mailing"
        ),
        InlineKeyboardButton(
            text="Отменить",
            callback_data="cancel_mailing"
        ),
    )
    builder.adjust(1)

    return builder.as_markup()


def mailing_message_button(
        buttons: list[list[str, str]]
) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for button in buttons:
        builder.add(
            InlineKeyboardButton(
                text=button[0],
                url=button[1],
            )
        )
        builder.adjust(1)

    return builder


def buttons_to_mailing_confirmation_with_buttons(
        buttons: list[list[str, str]]
):
    message_buttons_builder = mailing_message_button(buttons)

    message_buttons_builder.add(
        InlineKeyboardButton(
            text="Разослать",
            callback_data="mailing"
        ),
        InlineKeyboardButton(
            text="Отменить",
            callback_data="cancel_mailing"
        ),
    )

    message_buttons_builder.adjust(1)

    return message_buttons_builder.as_markup()


def add_buttons_to_builder(
        text: str,
        callback_data: str,
        builder: InlineKeyboardBuilder = None
) -> InlineKeyboardBuilder:

    if builder is None:
        builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text=text,
            callback_data=callback_data
        )
    )
    
    return builder
