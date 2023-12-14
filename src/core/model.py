from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class FilesID(Base):
    __tablename__ = "files_id"

    step2_1: Mapped[str]
    step2_2: Mapped[str]
    step2_3: Mapped[str]

    step3_1: Mapped[str]
    step3_2: Mapped[str]
    step3_3: Mapped[str]

    step5_vid: Mapped[str]

    step7_1: Mapped[str]
    step7_2_vid: Mapped[str]
    step7_3: Mapped[str]

    bonus1: Mapped[str]
    bonus2: Mapped[str]
    bonus3: Mapped[str]
