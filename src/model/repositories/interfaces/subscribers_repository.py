from abc import ABC, abstractmethod
from src.model.entities.participantes import Participantes

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None:
        pass
    
    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Participantes:
        pass