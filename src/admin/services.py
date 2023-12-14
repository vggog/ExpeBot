from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from src.admin.model import RefUrlModel
from src.admin.repository import AdminRepository
from src.core.repository import Repository
from src.admin.buttons import add_buttons_to_builder
from src.admin.utils import get_ref_url


class Services:
    repo = AdminRepository()

    def get_ref_links_button(
        self,
        start_callback_data: str
    ) -> InlineKeyboardBuilder:
        all_ref_urls = self.repo.get_all_ref_urls()

        builder = InlineKeyboardBuilder()
        for ref_url in all_ref_urls:
            add_buttons_to_builder(
                text=ref_url.name_ref_url,
                callback_data=start_callback_data + "_" + str(ref_url.id),
                builder=builder,
            )
        builder.adjust(1)

        return builder

    def get_buttons_by_profitability(self):
        builder = self.get_ref_links_button(
            "stat_ref_url"
        )

        add_buttons_to_builder(
            text="Общая статистика",
            callback_data="stat_ref_url_total",
            builder=builder,
        )
        builder.adjust(1)

        return builder.as_markup()

    def take_the_buttons_with_names_of_all_referral_links(
        self
    ) -> InlineKeyboardMarkup:
        builder = self.get_ref_links_button(
            "ref_url"
        )

        add_buttons_to_builder(
            text="Добавить реф. ссылку",
            callback_data="add_ref_url",
            builder=builder,
        )
        builder.adjust(1)

        return builder.as_markup()

    def generate_ref_url(self):
        count_of_ref_urls = self.repo.get_count_of_ref_url()

        return get_ref_url(count_of_ref_urls)

    def add_ref_url(self, ref_url_name, ref_url):
        ref_url_object = RefUrlModel(
            ref_url=ref_url,
            name_ref_url=ref_url_name
        )

        self.repo.add_ref_url(ref_url_object)

    def get_ref_url(self, data_from_callback: str):
        ref_url_id = data_from_callback.split("_")[2]
        ref_url = self.repo.get_ref_url(ref_url_id)

        return ref_url.ref_url

    def get_how_much_traffic(self) -> str:
        all_ref_urls = self.repo.get_all_ref_urls()
        traffic_str = ""
        for ref_url in all_ref_urls:
            traffic_str += f"<b>{ref_url.name_ref_url}</b>\n"
            users_traffic = self.repo.count_of_users(
                ref_url=ref_url.ref_url
            )
            users_lead = self.repo.count_of_users(
                ref_url=ref_url.ref_url,
                went_to_the_end=True,
            )
            traffic_str += f"traffic-[{users_traffic}] lead-[{users_lead}]"
            traffic_str += "\n"

        return traffic_str

    def get_statistic_on_route(self, callback_data: str) -> str:
        ref_url_id = callback_data.split("_")[3]

        core_repo = Repository()
        ref_url = self.repo.get_ref_url(ref_url_id)

        if ref_url_id == "total":
            stat1 = core_repo.get_count_of_user_from_step(start=True)
            stat2 = core_repo.get_count_of_user_from_step(step2=True)
            stat3 = core_repo.get_count_of_user_from_step(step3=True)
            stat4 = core_repo.get_count_of_user_from_step(step4=True)
            stat5 = core_repo.get_count_of_user_from_step(step5=True)
            stat6 = core_repo.get_count_of_user_from_step(step6=True)
            stat7 = core_repo.get_count_of_user_from_step(step7=True)
            stat8 = core_repo.get_count_of_user_from_step(step8=True)
            stat9 = core_repo.get_count_of_user_from_step(step9=True)
            stat10 = core_repo.get_count_of_user_from_step(step10=True)
            stat11 = core_repo.get_count_of_user_from_step(step11=True)
        else:
            stat1 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, start=True
            )
            stat2 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step2=True
            )
            stat3 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step3=True
            )
            stat4 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step4=True
            )
            stat5 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step5=True
            )
            stat6 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step6=True
            )
            stat7 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step7=True
            )
            stat8 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step8=True
            )
            stat9 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step9=True
            )
            stat10 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step10=True
            )
            stat11 = core_repo.get_count_of_user_from_step(
                ref_url=ref_url.ref_url, step11=True
            )

        return (
            "1) /start - " + str(stat1) + "\n" +

            "2) Что за реальность - " + str(stat2) + "\n" +

            "3) да - " + str(stat3) + "\n" +

            "4) Хочу подробнее - " + str(stat4) + "\n" +

            "5) Давай - " + str(stat5) + "\n" +

            "6) КТО ОН - " + str(stat6) + "\n" +

            "7) Сколько Зарабатывает - " + str(stat7) + "\n" +

            "8) Принять Приглашение - " + str(stat8) + "\n" +

            "9) Включить камеру(да/нет) - " + str(stat9) + "\n" +

            "10) Применить связку(да/нет) - " + str(stat10) + "\n" +

            "11) Дошел до конца(бонусы) - " + str(stat11) + "\n"
        )
