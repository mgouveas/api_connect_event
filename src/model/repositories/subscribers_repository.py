from src.model.configs.connection import DBConnectionHandler
from src.model.entities.participantes import Participantes

class SubscribersRepository:
    def insert(self, subscriber_infos: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Participantes(
                    nome=subscriber_infos.get("name"),
                    email=subscriber_infos.get("email"),
                    link=subscriber_infos.get("link"),
                    evento_id=subscriber_infos.get("evento_id")
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_subscriber(self, email: str, evento_id: int) -> Participantes:
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session
                    .query(Participantes)
                    .filter(Participantes.email == email, Participantes.evento_id == evento_id)
                    .one_or_none()
                )
                return data
            except Exception as exception:
                raise exception