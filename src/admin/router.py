import asyncio

import aiogram.exceptions
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, CallbackQuery, FSInputFile
)

from src.core.settings import Settings
from src.admin.buttons import (
    admin_menu_buttons, mailing_recipient_buttons,
    buttons_for_adding_mailing_buttons,
    buttons_to_mailing_confirmation_with_buttons, mailing_message_button
)
from src.admin.state import AdminStates, ButtonState, RefUrlState
from src.admin.mailing_data import MailingData
from src.utils import pars_raw_url_buttons
from src.core.repository import Repository
from src.admin.services import Services


admin_router = Router()


@admin_router.message(Command("admin"))
async def admin_menu(message: Message):
    if message.from_user.id in Settings.admins_id:
        await message.answer(
            "Админ панель",
            reply_markup=admin_menu_buttons(),
        )


@admin_router.callback_query(F.data == "newsletter")
async def newsletter_callback(callback: CallbackQuery) -> None:
    await callback.answer()

    MailingData.clear_data()
    await callback.message.answer(
        "Куда делаем рассылку?",
        reply_markup=mailing_recipient_buttons(),
    )


@admin_router.callback_query(F.data.in_(
    ["all_base", "who_went_to_end", "pick_up_all_bonus"]
))
async def newsletter_callback(
        callback: CallbackQuery,
        state: FSMContext
) -> None:
    await callback.answer()

    if callback.data == "all_base":
        MailingData.add_data(who_send="all")
    elif callback.data == "who_went_to_end":
        MailingData.add_data(who_send="went_to_end")
    elif callback.data == "pick_up_all_bonus":
        MailingData.add_data(who_send="pick_up_all_bonus")

    await callback.message.answer(
        "Отправьте боту то, что хотите разослать"
    )

    await state.set_state(AdminStates.what_to_mailing)


@admin_router.message(AdminStates.what_to_mailing)
async def what_to_mailing(message: Message, state: FSMContext) -> None:
    if message.text is not None:
        MailingData.add_data(
            message_type="text",
            source=message.text,
        )
        await message.answer(
            message.text,
            reply_markup=buttons_for_adding_mailing_buttons()
        )
    elif message.voice is not None:
        MailingData.add_data(
            message_type="voice",
            source=message.voice.file_id,
        )
        await message.answer_voice(
            message.voice.file_id,
            reply_markup=buttons_for_adding_mailing_buttons()
        )
    elif message.photo is not None:
        MailingData.add_data(
            message_type="photo",
            source=message.photo[-1].file_id,
        )
        await message.answer_photo(
            message.photo[-1].file_id,
            reply_markup=buttons_for_adding_mailing_buttons()
        )
    elif message.video is not None:
        MailingData.add_data(
            message_type="video",
            source=message.video.file_id,
        )
        await message.answer_video(
            message.video.file_id,
            reply_markup=buttons_for_adding_mailing_buttons()
        )
    elif message.video_note is not None:
        MailingData.add_data(
            message_type="video_note",
            source=message.video_note.file_id,
        )
        await message.answer_video_note(
            message.video_note.file_id,
            reply_markup=buttons_for_adding_mailing_buttons()
        )

    await state.clear()


@admin_router.callback_query(F.data == "add_mailing_buttons")
async def take_link_callback(
        callback: CallbackQuery,
        state: FSMContext
) -> None:
    await callback.answer()
    await callback.message.answer(
        "URL-КНОПКИ\n"
        "\n"
        "Отправьте боту список URL-кнопок в следующем формате:\n"
        "\n"
        "Кнопка1 - https://link.com\n"
        "Кнопка2 - https://link.com\n"
    )

    await state.set_state(ButtonState.message_with_url_button)


@admin_router.message(ButtonState.message_with_url_button)
async def what_to_mailing(message: Message, state: FSMContext) -> None:
    raw_url_buttons = message.text

    data = MailingData.add_data(url_buttons=message.text)

    if data["message_type"] == "text":
        await message.answer(
            data["source"],
            reply_markup=buttons_to_mailing_confirmation_with_buttons(
                buttons=pars_raw_url_buttons(raw_url_buttons)
            )
        )
    elif data["message_type"] == "voice":
        await message.answer_voice(
            data["source"],
            reply_markup=buttons_to_mailing_confirmation_with_buttons(
                buttons=pars_raw_url_buttons(raw_url_buttons)
            )
        )
    elif data["message_type"] == "photo":
        await message.answer_photo(
            data["source"],
            reply_markup=buttons_to_mailing_confirmation_with_buttons(
                buttons=pars_raw_url_buttons(raw_url_buttons)
            )
        )
    elif data["message_type"] == "video":
        await message.answer_video(
            data["source"],
            reply_markup=buttons_to_mailing_confirmation_with_buttons(
                buttons=pars_raw_url_buttons(raw_url_buttons)
            )
        )
    elif data["message_type"] == "video_note":
        await message.answer_video_note(
            data["source"],
            reply_markup=buttons_to_mailing_confirmation_with_buttons(
                buttons=pars_raw_url_buttons(raw_url_buttons)
            )
        )

    await state.clear()


@admin_router.callback_query(F.data == "mailing")
async def newsletter_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    repo = Repository()
    data = MailingData.get_data()

    if data["who_send"] == "went_to_end":
        users_to_mailing = repo.get_users_username(went_to_the_end=True)
    elif data["who_send"] == "pick_up_all_bonus":
        users_to_mailing = repo.get_users_username(pick_up_all_bonus=True)
    else:
        users_to_mailing = repo.get_users_username()

    await callback.message.answer(
        "Всего пользователей: " +
        str(len(users_to_mailing)) +
        "\n\n" +
        "Рассылка начата!"
    )

    if "url_buttons" in data:
        markup = mailing_message_button(
            pars_raw_url_buttons(data["url_buttons"])
        ).as_markup()
    else:
        markup = None

    count_of_users_to_sending = 0
    count_of_fail_to_sending = 0
    count_to_user_of_blocked = 0

    for user in users_to_mailing:
        user_id = user.id
        # users = [44520977, 678623761, 963139263, 1017120714, 1369858201]
        # if user_id in users:
        #     continue
        #
        # print(user_id)
        try:
            if data["message_type"] == "text":
                await callback.bot.send_message(
                    user_id,
                    data["source"],
                    reply_markup=markup
                )
            elif data["message_type"] == "voice":
                await callback.bot.send_voice(
                    user_id,
                    data["source"],
                    reply_markup=markup
                )
            elif data["message_type"] == "photo":
                await callback.bot.send_photo(
                    user_id,
                    data["source"],
                    reply_markup=markup
                )
            elif data["message_type"] == "video":
                await callback.bot.send_video(
                    user_id,
                    data["source"],
                    reply_markup=markup
                )
            elif data["message_type"] == "video_note":
                await callback.bot.send_video_note(
                    user_id,
                    data["source"],
                    reply_markup=markup
                )
        except aiogram.exceptions.TelegramBadRequest:
            count_of_fail_to_sending += 1
        except aiogram.exceptions.TelegramForbiddenError:
            count_to_user_of_blocked += 1
        else:
            count_of_users_to_sending += 1
        await asyncio.sleep(1)

    await callback.message.answer(
        "Рассылка окончено\n\n" +
        "Всего пользователей: " + str(len(users_to_mailing)) + "\n" +
        "Отправлено: " + str(count_of_users_to_sending) + "\n" +
        "Удалено пользователем: " + str(count_to_user_of_blocked) + "\n"
        "Произошло ошибок: " + str(count_of_fail_to_sending) + "\n"
    )

    MailingData.clear_data()


@admin_router.callback_query(F.data == "cancel_mailing")
async def cancel_mailing(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Рассылка отменена")


@admin_router.callback_query(F.data == "take_link")
async def take_link_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    service = Services()
    markup_to_answer = (
        service.take_the_buttons_with_names_of_all_referral_links()
    )
    await callback.message.answer(
        "Реферальные ссылки:",
        reply_markup=markup_to_answer,
    )


@admin_router.callback_query(F.data == "add_ref_url")
async def take_link_callback(
        callback: CallbackQuery,
        state: FSMContext
) -> None:
    await callback.answer()

    await callback.message.answer(
        "Напишите название вашей реферальной ссылки"
    )

    await state.set_state(RefUrlState.ref_url_title)


@admin_router.message(RefUrlState.ref_url_title)
async def what_to_mailing(message: Message, state: FSMContext) -> None:
    ref_url_title = message.text

    service = Services()
    ref_url = service.generate_ref_url()
    service.add_ref_url(
        ref_url_name=ref_url_title,
        ref_url=ref_url
    )

    await message.answer(
        "Ваша реферальная ссылка:\n\n" + ref_url
    )
    await state.clear()


@admin_router.callback_query(F.data.startswith("ref_url"))
async def profitability_statistics_callback(callback: CallbackQuery) -> None:
    await callback.answer()

    services = Services()
    ref_url = services.get_ref_url(callback.data)
    await callback.message.answer(
        "Ваша реферальная ссылка:\n\n" + ref_url
    )


@admin_router.callback_query(F.data == "profitability_statistics")
async def profitability_statistics_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    service = Services()
    await callback.message.answer(
        "Статистика",
        reply_markup=service.get_buttons_by_profitability()
    )


@admin_router.callback_query(F.data.startswith("stat_ref_url"))
async def profitability_statistics_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    service = Services()
    await callback.message.answer(
        service.get_statistic_on_route(callback.data)
    )


@admin_router.callback_query(F.data == "how_much_traffic")
async def how_much_traffic_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    services = Services()
    await callback.message.answer(
        services.get_how_much_traffic()
    )


@admin_router.callback_query(F.data == "download_database")
async def download_database_callback(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer_document(
        FSInputFile(Settings.db_path),
        caption="База данных всех пользователей."
    )
