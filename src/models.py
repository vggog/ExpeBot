from typing import Optional

from sqlalchemy import Column, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.core.model import Base


class Users(Base):
    __tablename__ = "users"

    name: Mapped[str]
    username: Mapped[str]
    user_url: Mapped[str]
    ref_url: Mapped[str]
    answer_first_question: Mapped[Optional[str]]
    answer_second_question: Mapped[Optional[str]]
    answer_third_question: Mapped[Optional[str]]
    answer_fourth_question: Mapped[Optional[str]]

    went_to_the_end: Mapped[bool] = Column(Boolean, default=False)
    pick_up_all_bonus: Mapped[bool] = Column(Boolean, default=False)


class UserPassability(Base):
    __tablename__ = "user_passability"

    user_id: Mapped[int]
    ref_url: Mapped[str]
    start: Mapped[bool] = mapped_column(default=True)
    step2: Mapped[bool] = mapped_column(default=False)
    step3: Mapped[bool] = mapped_column(default=False)
    step4: Mapped[bool] = mapped_column(default=False)
    step5: Mapped[bool] = mapped_column(default=False)
    step6: Mapped[bool] = mapped_column(default=False)
    step7: Mapped[bool] = mapped_column(default=False)
    step8: Mapped[bool] = mapped_column(default=False)
    step9: Mapped[bool] = mapped_column(default=False)
    step10: Mapped[bool] = mapped_column(default=False)
    step11: Mapped[bool] = mapped_column(default=False)
