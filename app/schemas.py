from typing import Optional
from pydantic import BaseModel

class Team(BaseModel):
    name: str

    class Config:
        orm_mode = True


class TeamPlayers(BaseModel):
    name: str
    position: str
    nation: str
    team: str
