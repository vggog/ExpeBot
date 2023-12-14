from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from src.core.settings import Settings
from src.models import Base


class DataBase:
    engine = create_engine(Settings.db_url)

    def _get_sessionmaker(self) -> sessionmaker:
        return sessionmaker(self.engine)

    def get_session(self) -> Session:
        session = self._get_sessionmaker()
        return session()

    def init_db(self):
        Base.metadata.create_all(self.engine)
