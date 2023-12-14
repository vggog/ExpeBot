from src.core.settings import Settings


def get_ref_url(url_id: str | int):
    return f"{Settings.bot_link}?start=ref-{url_id}"
