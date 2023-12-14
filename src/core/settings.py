import os
from dataclasses import dataclass

from dotenv import load_dotenv

from aiogram.types import FSInputFile

load_dotenv()


class Settings:
    bot_token: str = os.getenv("BOT_TOKEN")
    db_path: str = os.getenv("DB_PATH")
    db_url: str = os.getenv("SQLITE_PATH")
    chat_id: int = int(os.getenv("CHAT_ID"))
    admins_id: list[int] = list(map(int, os.getenv("ADMINS").split(", ")))
    admin = os.getenv("ADMIN")
    json_with_data: str = os.getenv("JSON_WITH_DATA")
    bot_link: str = os.getenv("LINK_TO_BOT")


class FilesPath:
    step1_picture = "static/1_start.jpg"
    step3_picture1 = "static/what_kind_of_reality1.jpg"
    step3_picture2 = "static/what_kind_of_reality2.jpg"
    step3_picture3 = "static/what_kind_of_reality3.jpg"
    step5_vidio = "static/step5_vid.mp4"

    step2_1 = "static/step2_1.jpg"
    step2_2 = "static/step2_2.jpg"
    step2_3 = "static/step2_3.jpg"

    step3_1 = "static/step3_1.jpg"
    step3_2 = "static/step3_2.jpg"
    step3_3 = "static/step3_3.jpg"

    step5_vid = "static/step5_vid.mp4"

    step7_1 = "static/step7_1.jpg"
    step7_2_vid = "static/step7_2_vid.mp4"
    step7_3 = "static/step7_3.jpg"

    bonus1 = "static/50 лидов за 5 мин в ТГ.pdf"
    bonus2 = "static/Идеальный лидмагнит.pdf"
    bonus3 = "static/11_способов_составления_гениального_оффера.pdf"


@dataclass
class FilesID:
    step2_1: str
    step2_2: str
    step2_3: str

    step3_1: str
    step3_2: str
    step3_3: str

    step5_vid: str

    step7_1: str
    step7_2_vid: str
    step7_3: str

    bonus1: str
    bonus2: str
    bonus3: str


@dataclass
class Files:
    step1_picture: FSInputFile
    step3_photo1: FSInputFile
    step3_photo2: FSInputFile
    step3_photo3: FSInputFile
    step5_vidio: FSInputFile


files = Files(
    step1_picture=FSInputFile(FilesPath.step1_picture),
    step3_photo1=FSInputFile(FilesPath.step3_picture1),
    step3_photo2=FSInputFile(FilesPath.step3_picture2),
    step3_photo3=FSInputFile(FilesPath.step3_picture3),
    step5_vidio=FSInputFile(FilesPath.step5_vidio),
)
