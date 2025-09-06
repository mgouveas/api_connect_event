from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class EventosLink(Base):
    __tablename__ = "Eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, nullable=False)
    evento_id = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
    participante_id = Column(Integer, ForeignKey("Participantes.id"), nullable=False)
