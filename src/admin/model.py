from sqlalchemy.orm import Mapped

from src.core.model import Base


class RefUrlModel(Base):
    __tablename__ = "ref_urls"

    ref_url: Mapped[str]
    name_ref_url: Mapped[str]
