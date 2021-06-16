from typing import Optional
from pydantic import BaseModel


class Players(BaseModel):
    idPlayer: Optional[int]
    name: str
    position: str
    nation: str
    team: str

    class Config:
    	orm_mode=True


class Team(BaseModel):
    name: str
    pages: Optional[int]    

class ResponseTeam(BaseModel):
    Page: int
    totalPages: int
    Items: int
    totalItems: int
    Players: dict

    class Config:
    	orm_mode=True