from src.core.database import DataBase
from src.models import Users, UserPassability

from src.core.model import FilesID


class Repository:
    db = DataBase()

    def create_user(self, user: Users, user_passability: UserPassability):
        with self.db.get_session() as session:
            session.add(user)
            session.add(user_passability)
            session.commit()

    def get_user(self, user_id):
        with self.db.get_session() as session:
            return session.query(Users).filter_by(id=user_id).first()

    def update_user(self, user_id, **kwargs):
        with self.db.get_session() as session:
            session.query(Users).filter_by(id=user_id).update(kwargs)
            session.commit()

    def get_users_username(self, **filters):
        with self.db.get_session() as session:
            return session.query(Users).filter_by(**filters).all()

    def update_user_passability(self, user_id, **filters):
        with self.db.get_session() as session:
            session.query(UserPassability).filter_by(
                user_id=user_id
            ).update(filters)
            session.commit()

    def get_count_of_user_from_step(self, **kwargs) -> int:
        with self.db.get_session() as session:
            return session.query(UserPassability).filter_by(**kwargs).count()

    def add_files_id(self, files_id_model):
        with self.db.get_session() as session:
            session.query(FilesID).delete()

            session.add(files_id_model)
            session.commit()

    def get_files_ids(self) -> FilesID:
        with self.db.get_session() as session:
            return session.query(FilesID).first()
