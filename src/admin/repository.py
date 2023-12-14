from src.core.database import DataBase
from src.admin.model import RefUrlModel
from src.models import Users


class AdminRepository:
    db = DataBase()

    def get_ref_url(self, ref_url_id):
        with self.db.get_session() as session:
            return session.query(RefUrlModel).filter_by(id=ref_url_id).first()

    def get_all_ref_urls(self) -> list:
        with self.db.get_session() as session:
            return session.query(RefUrlModel).all()

    def get_count_of_ref_url(self) -> int:
        with self.db.get_session() as session:
            return session.query(RefUrlModel).count()

    def add_ref_url(self, ref_url: RefUrlModel):
        with self.db.get_session() as session:
            session.add(ref_url)
            session.commit()

    def count_of_users(self, **filters) -> int:
        with self.db.get_session() as session:
            return session.query(Users).filter_by(**filters).count()

    def get_ref_url_name(self, ref_url) -> str:
        with self.db.get_session() as session:
            return session.query(RefUrlModel).filter_by(
                ref_url=ref_url
            ).first().name_ref_url
