from pydantic import BaseModel, HttpUrl
from typing import Optional

class Course(BaseModel):
    id: str
    name: str
    code: str
    category_id: str
    description: str
    price: str
    status: str
    creation_date: str
    last_update_on: str
    creator_id: str
    hide_from_catalog: str
    time_limit: str
    start_datetime: Optional[str] = None
    expiration_datetime: Optional[str] = None
    level: Optional[str] = None
    shared: str
    shared_url: Optional[str] = ""
    avatar: HttpUrl
    big_avatar: HttpUrl
    certification: Optional[str] = None
    certification_duration: Optional[str] = None
