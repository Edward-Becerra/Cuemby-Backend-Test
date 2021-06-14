# Archivo para definir el modelo de la tabla de la base de datos

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .conexion import Base


class Players(Base):
    __tablename__ = "players"
    idPlayer = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    position = Column(String(10))
    nation  = Column(String(45))
    team = Column(String(45))

