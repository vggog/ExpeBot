import cv2

from src.models import Users
from src.admin.repository import AdminRepository


def get_yes_or_no(message: str) -> str:
    """
    Парсинг строки для получение ответов Да или Нет.
    :param message: Строка вида <чтото_yes> или <чтото_no>
    :return: строку "Да" или "Нет"
    """
    answer = message.split("_")[-1]

    return "Да" if answer == "yes" else "Нет"


def get_message_of_user_info(user: Users) -> str:
    """
    Строка информации о пользователе,
    отправляемая в чат для дальнейшей взаимодействии с пользователем.
    :param user: Модель пользователе,
        откуда получается вся информация о пользователе.
    """
    repo = AdminRepository()
    try:
        ref_url_name = repo.get_ref_url_name(user.ref_url)
    except AttributeError:
        ref_url_name = "Зашёл без реферальной ссылки."
    message = (
        '<b>ЗАЯВКА ОТ </b>➡️ <a href="{user_url}">{user_name}</a>\n'
        'username - @{username}\n'
        'ссылка - {user_url2}'
        '\n'
        '🗿<b>Хто↓</b>\n'
        'Ответ: {answer_first_question}\n'
        '\n'
        '🤑 <b>Сколько хаслит бабок ↓</b>\n'
        'Ответ: {answer_second_question}\n'
        '\n'
        '📸 <b>Камеру врубит ↓</b>\n'
        'Ответ: {answer_third_question}\n'
        '\n'
        '🤪 <b>Готов принимать, чтобы улететь ↓</b>\n'
        'Ответ: {answer_fourth_question}\n'
        '\n'
        'Лид пришёл от - {ref_url_name}\n'
    ).format(
        user_url=user.user_url,
        user_name=user.name,
        username=user.username,
        user_url2=user.user_url,
        answer_first_question=user.answer_first_question,
        answer_second_question=user.answer_second_question,
        answer_third_question=user.answer_third_question,
        answer_fourth_question=user.answer_fourth_question,
        ref_url_name=ref_url_name
    )

    return message


def get_width_height_of_the_video(vidio_path: str) -> dict:
    """
    Метод для определения длинны и высоты видео.
    :param vidio_path: путь до файла, у которого надо узнать высоту и ширину.
    :return: dict{
        "height": float,
        "width": float
    }
    """
    file_path = vidio_path
    vid = cv2.VideoCapture(file_path)
    return {
        'height': vid.get(cv2.CAP_PROP_FRAME_HEIGHT),
        'width': vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    }


def pars_raw_url_buttons(raw_url_buttons: str) -> list[list[str, str]]:
    """
    Метод, для парсинга текста содержащий кнопки и ссылки на кнопки.
    текст должен быть представлен в формате
        <кнопка> - <ссылка>
        <кнопка> - <ссылка>
        ...
    :param raw_url_buttons: текст, со строками вида <кнопка - ссылка>
    :return: list[list[<кнопка>, <ссылка>]]
    """
    return list(
        map(
            lambda s: s.split(" - "), raw_url_buttons.split("\n")
        )
    )
