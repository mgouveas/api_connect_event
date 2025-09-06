from sqlalchemy import func, desc
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.participantes import Participantes
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
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
            
    def select_subscribers_by_link(self, link: str, event_id: int) -> list:
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session
                    .query(Participantes)
                    .filter(Participantes.link == link, Participantes.evento_id == event_id)
                    .all()
                )
                return data
            except Exception as exception:
                raise exception
            
    def get_ranking(self, event_id: int) -> list:
        with DBConnectionHandler() as db:
            try:
                result = (
                    db.session
                    .query(
                        Participantes.link, 
                        func.count(Participantes.id).label("total")
                    )
                    .filter(
                        Participantes.evento_id == event_id, 
                        Participantes.link.isnot(None)
                    )
                    .group_by(Participantes.link)
                    .order_by(desc("total"))
                    .all()
                ) 
                return result
            except Exception as exception:
                raise exception