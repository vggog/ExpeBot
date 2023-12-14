from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile

from src.core.settings import Settings

from src.routers import main_routers
from src.admin.router import admin_router

from src.core.model import FilesID
from src.core.settings import FilesPath
from src.core.repository import Repository


class BotFactory:

    @staticmethod
    async def start_bot():
        dp = Dispatcher()
        dp.include_routers(
            main_routers,
            admin_router,
        )

        bot = Bot(Settings.bot_token, parse_mode=ParseMode.HTML)
        print("Загрузка файлов.")
        await BotFactory.upload_all_files(bot)
        print("Загрузка завершена.")
        await dp.start_polling(bot)

    @staticmethod
    async def upload_all_files(bot: Bot):
        repo = Repository()

        step2_1_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step2_1)
        )
        step2_2_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step2_2)
        )
        step2_3_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step2_3)
        )
        step3_1_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step3_1)
        )
        step3_2_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step3_2)
        )
        step3_3_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step3_3)
        )
        step7_1_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step7_1)
        )
        step7_3_file_id = await bot.send_photo(
            Settings.admin,
            FSInputFile(FilesPath.step7_3)
        )

        step5_vid_file_id = await bot.send_video(
            Settings.admin,
            FSInputFile(FilesPath.step5_vid)
        )
        step7_2_vid_file_id = await bot.send_video(
            Settings.admin,
            FSInputFile(FilesPath.step7_2_vid)
        )

        bonus1_file_id = await bot.send_document(
            Settings.admin,
            FSInputFile(FilesPath.bonus1)
        )
        bonus2_file_id = await bot.send_document(
            Settings.admin,
            FSInputFile(FilesPath.bonus2)
        )
        bonus3_file_id = await bot.send_document(
            Settings.admin,
            FSInputFile(FilesPath.bonus3)
        )

        # print(bonus1_file_id, "\n\n\n")
        # return

        files_id = FilesID(
            step2_1=step2_1_file_id.photo[0].file_id,
            step2_2=step2_2_file_id.photo[0].file_id,
            step2_3=step2_3_file_id.photo[0].file_id,

            step3_1=step3_1_file_id.photo[0].file_id,
            step3_2=step3_2_file_id.photo[0].file_id,
            step3_3=step3_3_file_id.photo[0].file_id,

            step5_vid=step5_vid_file_id.video.file_id,

            step7_1=step7_1_file_id.photo[0].file_id,
            step7_2_vid=step7_2_vid_file_id.video.file_id,
            step7_3=step7_3_file_id.photo[0].file_id,

            bonus1=bonus1_file_id.document.file_id,
            bonus2=bonus2_file_id.document.file_id,
            bonus3=bonus3_file_id.document.file_id,
        )

        repo.add_files_id(files_id)
