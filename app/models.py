# Archivo para definir el modelo de la tabla de la base de datos

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .conexion import Base


class Players(Base):
    __tablename__ = "Players"
    idPlayer = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    posicion = Column(String(20))
    nation  = Column(String(100))
    team = relationship("Teams")

class Teams(Base):
    __tablename__="Teams"
    idTeam = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    idPlayer = Column(
        Integer, ForeignKey("Players.idPlayer", ondelete="CASCADE"), nullable=False
    )
