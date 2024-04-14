from pydantic import BaseModel
from datetime import date

class activities(BaseModel):
    activity_id: int
    activity_type: str
    activity_name: str
    description: str