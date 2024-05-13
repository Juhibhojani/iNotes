from pydantic import BaseModel

class note(BaseModel):
    title:str
    desc:str
    important:bool