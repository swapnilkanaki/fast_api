from pydantic import BaseModel

class dataUse(BaseModel):
    id: int
    region: str
    data: int
    lat: float
    lng:float