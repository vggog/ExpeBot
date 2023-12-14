import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message, CallbackQuery, FSInputFile
)

from src.buttons import (
    one_inline_button, average_income_buttons, yes_no_buttons,
    what_are_you_doing_button, no_step10_buttons
)
from src.utils import (
    get_yes_or_no, get_message_of_user_info, get_width_height_of_the_video
)
from src.core.repository import Repository
from src.models import Users, UserPassability
from src.core.settings import Settings, FilesPath


main_routers = Router()


@main_routers.message(Command("get_chat_id"))
async def set_chat_id(message: Message) -> None:
    if message.from_user.id == 645807089:
        await message.answer(f"id чата: \n{message.chat.id}")


@main_routers.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    try:
        ref_url = Settings.bot_link + "?start=" + message.text.split(" ")[1]
    except IndexError:
        ref_url = Settings.bot_link + "?start"

    repo = Repository()
    if not repo.get_user(message.from_user.id):
        if message.from_user.username:
            user_username = message.from_user.username
        else:
            user_username = "Безымянный"

        user = Users(
            id=message.from_user.id,
            name=message.from_user.first_name,
            username=user_username,
            user_url=message.from_user.url,
            ref_url=ref_url
        )
        user_passability = UserPassability(
            user_id=message.from_user.id,
            ref_url=ref_url
        )

        repo.create_user(user, user_passability)

    await message.answer(
        "Ты тут 105% не случайно👌\n\nУ меня есть для тебя новая реальность",
        reply_markup=one_inline_button(
            text="Что за реальность?",
            callback_data="step2",
        )
    )


@main_routers.callback_query(F.data == "step2")
async def step2(callback: CallbackQuery) -> None:
    await callback.answer()

    repo = Repository()
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step2=True,
    )

    files_id = repo.get_files_ids()

    # photo1 = FSInputFile("static/step2_1.jpg")
    await callback.message.answer_photo(photo=files_id.step2_1)
    await asyncio.sleep(2)
    # photo2 = FSInputFile("static/step2_2.jpg")
    await callback.message.answer_photo(photo=files_id.step2_2)
    await asyncio.sleep(2)
    # photo3 = FSInputFile("static/step2_3.jpg")
    await callback.message.answer_photo(photo=files_id.step2_3)
    await asyncio.sleep(2)

    await callback.message.answer(
        "Интересно?",
        reply_markup=one_inline_button(
            text="Да",
            callback_data="step3"
        )
    )


@main_routers.callback_query(F.data == "step3")
async def step3(callback: CallbackQuery) -> None:
    """
    """
    await callback.answer()

    repo = Repository()
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step3=True,
    )

    files_id = repo.get_files_ids()

    await callback.message.answer_sticker(
        "CAACAgIAAxkBAAECbm9lefsxoXG7sERvlchn"
        "7zBvRProOgACN0UAAjskqUsGhzxzCywwGjME"
    )
    await asyncio.sleep(1)

    await callback.message.answer_sticker(
        "CAACAgIAAxkBAAECbndleftRH5ByQLxKpnk8"
        "ktKbw27ArwACQUcAAnnmqUs_jcmhPWt1PzME"
    )
    await asyncio.sleep(1)

    await callback.message.answer_sticker(
        "CAACAgIAAxkBAAECbnlleftbMM-d0yZfb3Dn"
        "_5wn-pGEMQACBEMAAu6DqEtSK_1m1477czME"
    )
    await asyncio.sleep(1)

    await callback.message.answer_sticker(
        "CAACAgIAAxkBAAEBOgRlFHTvvm6TQs_kbpOJ"
        "lkpYIAzdlgACtzYAAjJ50UtuaZMXZQNWeTAE"
    )
    await asyncio.sleep(1)

    # photo1 = FSInputFile("static/step3_1.jpg")
    await callback.message.answer_photo(
        photo=files_id.step3_1,
        caption=(
            '<a href="https://t.me/nikola_disney/292">Смотреть</a>'
        ),
        parse_mode="HTML",
    )
    # photo2 = FSInputFile("static/step3_2.jpg")
    await callback.message.answer_photo(
        photo=files_id.step3_2,
        caption=(
            '<a href="https://t.me/nikola_disney/325">Смотреть</a>'
        ),
        parse_mode="HTML",
    )
    # photo3 = FSInputFile("static/step3_3.jpg")
    await callback.message.answer_photo(
        photo=files_id.step3_3,
        caption=(
            '<a href="https://t.me/nikola_disney/296">Смотреть</a>'
        ),
        parse_mode="HTML",
    )

    await asyncio.sleep(2)

    await callback.message.answer(
        "Да, тут всё реально! Как посмотришь кейсы\n"
        "Жми на кнопку 👇🏻",
        reply_markup=one_inline_button(
            text="Хочу подробнее",
            callback_data="step4",
        )
    )


@main_routers.callback_query(F.data == "step4")
async def step4(callback: CallbackQuery) -> None:
    await callback.answer()
    repo = Repository()
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step4=True,
    )
    files_id = repo.get_files_ids()

    await callback.message.answer("…сейчас я вас познакомлю =)")
    await asyncio.sleep(2)

    vidio_size = get_width_height_of_the_video(FilesPath.step5_vid)

    await callback.message.answer_video(
        video=files_id.step5_vid,
        width=vidio_size["width"],
        height=vidio_size["height"],
        # thumbnail=FSInputFile("static/step5_vid_prev.JPEG"),
        caption=
        "Никола Дисней \n"
        "\n"
        "<b>Создатель</b> новой модели запусков и "
        "продаж на высокий чек - <b>EXPE</b>\n"
        "\n"
        "- сделал на охватах 70 человек - <b>8,5 млн ₽ за 3 месяца</b>, "
        "благодаря технологии EXPE\n"
        "\n"
        "- обучил 50+ учеников, которые по его модели заработали <b>1-3 млн ₽ "
        "за 3 недели</b>\n"
        "\n"
        "<b>- выработал собственную систему запуска от 1 млн ₽ за 3 недели</b>"
        " (без вложений в трафик и маркетинг)"
    )

    await asyncio.sleep(4)
    await callback.message.answer(
        "Давай я тебе расскажу, как ты сделаешь такой результат?",
        reply_markup=one_inline_button(
            text="Давай 🚀",
            callback_data="step5",
        )
    )


@main_routers.callback_query(F.data == "step5")
async def step5(callback: CallbackQuery) -> None:
    await callback.answer()

    repo = Repository()
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step5=True,
    )

    await callback.message.answer(
        "Ой 😅 да я о тебе ещё ничего не знаю,\n"
        "расскажи немного о себе\n"
        "\n"
        "Ты…",
        reply_markup=what_are_you_doing_button(),
    )


@main_routers.callback_query(F.data.startswith("step6"))
async def step6(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    repo = Repository()

    actions = {
        '1': 'Предприниматель',
        '2': 'Продюсер',
        '3': 'Эксперт',
        '4': 'Наставник',
        '5': 'Маркетолог',
        '6': 'Блогер',
        '7': 'Работа в найме',
        '8': 'Другое',
        '9': 'Инфопредприниматель',
    }
    action = callback.data.split("_")[1]
    answer = actions[action]
    repo.update_user(
        callback.from_user.id,
        answer_first_question=answer
    )

    await callback.message.answer(
        "<b>Какой твой средний доход в месяц?</b>",
        reply_markup=average_income_buttons(),
    )
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step6=True,
    )


@main_routers.callback_query(F.data.startswith("step7"))
async def step7(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete()

    repo = Repository()

    repo.update_user_passability(
        user_id=callback.from_user.id,
        step7=True,
    )

    action = callback.data.split("_")[1]
    if action == "1":
        answer = "До 100 тысяч (1000$)"
    elif action == "2":
        answer = "От 100 до 300 тысяч (3000$)"
    elif action == "3":
        answer = "От 300 до 600 тысяч (6000$)"
    elif action == "4":
        answer = "От 600 до 1 млн (10000$)"
    else:
        answer = "Больше 1 млн (10.000$+)"

    repo.update_user(
        callback.from_user.id,
        answer_second_question=answer
    )

    await callback.message.answer("Отлично 🔥")
    await asyncio.sleep(1)

    await callback.message.answer(
        "Такс.. Вот те самые 3 шага ↓"
    )
    # await asyncio.sleep(3)

    # photo1 = FSInputFile("static/step7_1.jpg")
    files_id = repo.get_files_ids()
    await callback.message.answer_photo(
        photo=files_id.step7_1,
        caption=
        'Вы <b>терпите поражение</b> ещё до того, '
        'как решили <b>сделать продажу</b>!\n'
        '\n'
        '<span class="tg-spoiler">'
        'Если вы делаете это <b>БЕЗ</b> качественной маркетинг распаковки '
        '</span>',
        parse_mode="HTML"
    )
    await asyncio.sleep(2)

    # await callback.message.answer("Второй шаг ↓")
    # await asyncio.sleep(1)

    vidio_size = get_width_height_of_the_video(FilesPath.step7_2_vid)
    # video2 = FSInputFile("static/step7_2_vid.mp4")

    await callback.message.answer_video(
        video=files_id.step7_2_vid,
        width=vidio_size["width"],
        height=vidio_size["height"],
        caption=
        '<span class="tg-spoiler">'
        'Формируем <b>убойный</b> оффер и настраиваем лидо-систему так, '
        'чтобы <b>заявки шли каждый день</b>'
        '</span>',
        parse_mode="HTML"
    )
    await asyncio.sleep(2)

    # await callback.message.answer("Третий шаг ↓")
    # await asyncio.sleep(1)
    # photo3 = FSInputFile("static/step7_3.jpg")
    await callback.message.answer_photo(
        photo=files_id.step7_3,
        caption=
        '<span class="tg-spoiler">'
        'Заработать один раз может каждый, '
        'а повторять из раза в раз? Единицы=)'
        '</span>',
        parse_mode="HTML"
    )
    await asyncio.sleep(2)

    await callback.message.answer(
        "<b>Приглашаю тебя в гости</b> 🥳\n"
        "Давай по полочкам разберём твою ситуацию и ты узнаешь, "
        "как мы построим тебе трафик-систему так, "
        "чтобы заявки были каждый день",
        reply_markup=one_inline_button(
            text="Принять приглашение ✅",
            callback_data="step8",
        )
    )


@main_routers.callback_query(F.data == "step8")
async def step8(callback: CallbackQuery) -> None:
    await callback.answer()
    repo = Repository()

    repo.update_user_passability(
        user_id=callback.from_user.id,
        step8=True,
    )

    await callback.message.answer(
        'Отлично, поздравляю! 🙌🏽\n'
        '\n'
        'Я запишу тебя на видеовстречу\n'
        '\n'
        '*Готов(а) включить камеру, чтобы созвониться?*',
        parse_mode="Markdown",
        reply_markup=yes_no_buttons(
            "step9"
        ),
    )


@main_routers.callback_query(F.data.startswith("step9"))
async def step9(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    repo = Repository()
    repo.update_user(
        callback.from_user.id,
        answer_third_question=get_yes_or_no(callback.data),
    )
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step9=True,
    )

    if callback.data == "step9_yes":
        await callback.message.answer(
            '*Готов(а) применять связки и стратегии Николы, '
            'чтобы выйти на новый уровень?*',
            parse_mode="Markdown",
            reply_markup=yes_no_buttons(
                "step10"
            ),
        )
    else:
        video_path = 'static/step12.mp4'
        vidio_size = get_width_height_of_the_video(video_path)
        vidio = FSInputFile(video_path)
        await callback.message.answer_video(
            video=vidio,
            width=vidio_size["width"],
            height=vidio_size["height"],
            caption="Поздравляю!\nВаша возможность почти проср*на 😥",
        )
        await asyncio.sleep(4)
        await callback.message.answer(
            "Готов(а) применять связки и стратегии Николы, "
            "чтобы выйти на новый уровень?",
            reply_markup=yes_no_buttons(
                "answer_no_step10"
            )
        )


@main_routers.callback_query(F.data.startswith("step10"))
async def step10(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    repo = Repository()
    repo.update_user(
        callback.from_user.id,
        answer_fourth_question=get_yes_or_no(callback.data),
    )
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step10=True,
    )

    user = repo.get_user(callback.from_user.id)
    if user:
        await callback.bot.send_message(
            Settings.chat_id,
            get_message_of_user_info(user)
        )

    repo = Repository()
    repo.update_user(
        callback.from_user.id,
        went_to_the_end=True,
    )

    if callback.data == "step10_yes":
        await callback.message.answer(
            "<b>Твоя заявка принята!\n" 
            "В скором времени с тобой свяжутся 🥳</b>\n"
            "\n"
            "А пока что держи:\n"
            "\n"
            "<a "
            "href=\"https://teletype.in/@nikola_disney/klient_za_3_million\""
            ">🎁 КАК ПРИВЛЕЧЬ КЛИЕНТА НА ЧЕК 1-3 млн ₽"
            "</a>",
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=one_inline_button(
                "Хочу ещё",
                "step11"
            )
        )
    else:
        video_path = 'static/step12.mp4'
        vidio_size = get_width_height_of_the_video(video_path)
        vidio = FSInputFile(video_path)
        await callback.message.answer_video(
            video=vidio,
            width=vidio_size["width"],
            height=vidio_size["height"],
            caption="Поздравляю!\nВаша возможность проср*на 😥",
        )
        await asyncio.sleep(4)

        await callback.message.answer(
            "У тебя была возможность получить "
            "*бесплатно* "
            "стратегическую сессию у Николы\n"
            "Теперь она платная =)",
            parse_mode="markdown",
            reply_markup=no_step10_buttons(),
        )


@main_routers.callback_query(F.data == "step11")
async def step11(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    await callback.message.answer(
        "Супер, держи\n"
        "\n"
        "<a href=\"https://teletype.in/@nikola_disney/1100000za3dnya\">"
        "🎁 Как сделать 1.100.000₽ на трёхдневном прогреве</a>",
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=one_inline_button(
            "Хочу ещё",
            "step11_1"
        )
    )

    repo = Repository()
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step11=True,
    )


@main_routers.callback_query(F.data == "step11_1")
async def step11_1(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    repo = Repository()
    files_id = repo.get_files_ids()

    # file = FSInputFile("static/50 лидов за 5 мин в ТГ.pdf")
    await callback.message.answer("Без проблем 😉 \nдержи")
    await callback.message.answer_document(
        files_id.bonus1,
        reply_markup=one_inline_button(
            "А я хочу ещё 😃",
            "step11_2"
        )
    )


@main_routers.callback_query(F.data == "step11_2")
async def step11_2(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    repo = Repository()
    files_id = repo.get_files_ids()

    # file = FSInputFile("static/Идеальный лидмагнит.pdf")
    await callback.message.answer("Хорошо 👌🏼 забирай ещё =)")
    await callback.message.answer_document(
        files_id.bonus2,
        reply_markup=one_inline_button(
            "А можно ещё?",
            "step11_3"
        )
    )


@main_routers.callback_query(F.data == "step11_3")
async def step11_3(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    repo = Repository()
    files_id = repo.get_files_ids()

    # file = FSInputFile("static/11_способов_составления_гениального_оффера.pdf")
    await callback.message.answer("Да можно ещё =) держи")
    await callback.message.answer_document(
        files_id.bonus3,
        reply_markup=one_inline_button(
            "И ещё один разок ☝🏽 ладно? 😅",
            "step11_4"
        )
    )


@main_routers.callback_query(F.data == "step11_4")
async def step11_3(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    await callback.message.answer(
        "А «ещё разок» ты получишь лично у Николы\n"
        "\n"
        "…если он тебя отберет на разбор"
    )

    repo = Repository()
    repo.update_user(
        callback.from_user.id,
        pick_up_all_bonus=True,
    )


@main_routers.callback_query(F.data.startswith("answer_no_step10"))
async def step8(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    if callback.data == "answer_no_step10_no":
        photo = FSInputFile("static/step13.jpg")
        await callback.message.answer_photo(
            photo,
            caption="Ваш лимит доверия исчерпан!\n"
                    "\n"
                    "Возможность стать богаче упущена\n"
                    "\n"
                    "- мы ценим нелегкий труд, поэтому оставайтесь там, "
                    "где он пригодится! ❤️"
        )
        await asyncio.sleep(4)

    await callback.message.answer(
        "У тебя была возможность получить "
        "*бесплатно* "
        "стратегическую сессию у Николы\n"
        "Теперь она платная =)",
        parse_mode="markdown",
        reply_markup=no_step10_buttons(),
    )

    repo = Repository()
    repo.update_user(
        callback.from_user.id,
        answer_fourth_question=get_yes_or_no(callback.data),
        went_to_the_end=True,
    )

    user = repo.get_user(callback.from_user.id)
    if user:
        await callback.bot.send_message(
            Settings.chat_id,
            get_message_of_user_info(user)
        )


@main_routers.callback_query(F.data == "sign_up_strat_session")
async def sign_up_strat_session(callback: CallbackQuery) -> None:
    await callback.answer()

    await callback.message.answer(
        "Стоимость стратегической сессии\n"
        "\n"
        "- 201 USDT\n"
        "\n"
        "После оплаты пиши сюда - @nikoIanext\n" 
        "\n"
        "- Сеть (TRC20)\n"
        "\n"
        "TBvWrmTvvJCnTWRBaUPZR3eGTQQ4LrAJiu"
    )
    await callback.message.answer(
        "TBvWrmTvvJCnTWRBaUPZR3eGTQQ4LrAJiu"
    )


@main_routers.callback_query(F.data == "pick_up_bonuses")
async def step11(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    await callback.message.answer(
        "Супер, держи\n"
        "\n"
        "<a href=\"https://teletype.in/@nikola_disney/1100000za3dnya\">"
        "🎁 Как сделать 1.100.000₽ на трёхдневном прогреве</a>",
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=one_inline_button(
            "Хочу ещё",
            "pick_up_bonuses_1"
        )
    )

    repo = Repository()
    repo.update_user_passability(
        user_id=callback.from_user.id,
        step11=True,
    )


@main_routers.callback_query(F.data == "pick_up_bonuses_1")
async def pick_up_bonuses_1(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    file = FSInputFile("static/50 лидов за 5 мин в ТГ.pdf")
    await callback.message.answer("Без проблем 😉 \nдержи")
    await callback.message.answer_document(
        file,
        reply_markup=one_inline_button(
            "А я хочу ещё 😃",
            "pick_up_bonuses_2"
        )
    )


@main_routers.callback_query(F.data == "pick_up_bonuses_2")
async def pick_up_bonuses_2(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    file = FSInputFile("static/Идеальный лидмагнит.pdf")
    await callback.message.answer("Хорошо 👌🏼 забирай ещё =)")
    await callback.message.answer_document(
        file,
        reply_markup=one_inline_button(
            "А можно ещё?",
            "pick_up_bonuses_3"
        )
    )


@main_routers.callback_query(F.data == "pick_up_bonuses_3")
async def pick_up_bonuses_3(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    file = FSInputFile("static/11_способов_составления_гениального_оффера.pdf")
    await callback.message.answer("Да можно ещё =) держи")
    await callback.message.answer_document(
        file,
        reply_markup=one_inline_button(
            "И ещё один разок ☝🏽 ладно? 😅",
            "pick_up_bonuses_4"
        )
    )


@main_routers.callback_query(F.data == "pick_up_bonuses_4")
async def pick_up_bonuses_4(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.delete_reply_markup()

    await callback.message.answer(
        "А «ещё разок» ты получишь лично у Николы =)",
        reply_markup=one_inline_button(
            "Записаться на Страт.сессию",
            "sign_up_strat_session",
        )
    )
