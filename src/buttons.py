from aiogram.utils.keyboard import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardBuilder
)


def one_inline_button(
        text: str,
        callback_data: str,
):
    button = InlineKeyboardButton(
        text=text,
        callback_data=callback_data
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return markup


def average_income_buttons():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="До 100 тысяч (1000$)",
            callback_data="step7_1"
        ),
        InlineKeyboardButton(
            text="От 100 до 300 тысяч (3000$)",
            callback_data="step7_2"
        ),
        InlineKeyboardButton(
            text="От 300 до 600 тысяч (6000$)",
            callback_data="step7_3"
        ),
        InlineKeyboardButton(
            text="От 600 до 1 млн (10000$)",
            callback_data="step7_4"
        ),
        InlineKeyboardButton(
            text="Больше 1 млн (10.000$+)",
            callback_data="step7_5"
        ),
    )

    builder.adjust(1)

    return builder.as_markup()


def yes_no_buttons(step: str):
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="✅ Да ",
            callback_data=step + "_yes"
        ),
        InlineKeyboardButton(
            text="❌ Нет",
            callback_data=step + "_no"
        ),
    )

    return builder.as_markup()


def what_are_you_doing_button():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Предприниматель",
            callback_data="step6_1"
        ),
        InlineKeyboardButton(
            text="Продюсер",
            callback_data="step6_2"
        ),
    )
    builder.row(
        InlineKeyboardButton(
            text="Эксперт",
            callback_data="step6_3"
        ),
        InlineKeyboardButton(
            text="Наставник",
            callback_data="step6_4"
        ),
    )

    builder.row(
        InlineKeyboardButton(
            text="Маркетолог",
            callback_data="step6_5"
        ),
        InlineKeyboardButton(
            text="Блогер",
            callback_data="step6_6"
        ),
    )
    builder.row(
        InlineKeyboardButton(
            text="Работа в найме",
            callback_data="step6_7"
        ),
        InlineKeyboardButton(
            text="Другое",
            callback_data="step6_8"
        ),
    )

    builder.row(
        InlineKeyboardButton(
            text="Инфопредприниматель",
            callback_data="step6_9"
        ),
    )

    return builder.as_markup()


def no_step10_buttons():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Записаться на Страт.сессию",
            callback_data="sign_up_strat_session"
        ),
        InlineKeyboardButton(
            text="Забрать взрывные бонусы",
            callback_data="pick_up_bonuses"
        ),
    )

    builder.adjust(1)

    return builder.as_markup()
