import json

from src.core.settings import Settings


class MailingData:
    @staticmethod
    def get_data() -> dict:
        with open(Settings.json_with_data, "r") as f:
            return json.load(f)

    @staticmethod
    def add_data(**kwargs) -> dict:
        data = MailingData.get_data()
        data.update(**kwargs)
        with open(Settings.json_with_data, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return data

    @staticmethod
    def clear_data():
        with open(Settings.json_with_data, "w") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
