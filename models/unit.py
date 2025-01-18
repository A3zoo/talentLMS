#Unit này sẽ là các bài test, survey,...

from pydantic import BaseModel, HttpUrl

class Unit(BaseModel):
    id: int
    type: str
    name: str
    url: HttpUrl
