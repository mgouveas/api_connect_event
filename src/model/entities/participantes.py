from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Participantes(Base):
    __tablename__ = "Participantes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
