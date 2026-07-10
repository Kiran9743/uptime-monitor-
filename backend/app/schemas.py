from pydantic import BaseModel, HttpUrl
from typing import Optional
import datetime

class MonitorCreate(BaseModel):
    name: str
    url: HttpUrl

class MonitorRead(BaseModel):
    id: int
    name: str
    url: HttpUrl
    last_checked: Optional[datetime.datetime]
    status: str

    class Config:
        orm_mode = True
