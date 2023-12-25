from abc import ABC
from typing import Optional

import pydantic


class AbstractAdvert(pydantic.BaseModel, ABC):
    title: str
    text: str

class CreateAdvert(AbstractAdvert):
    author_id: int
    title: str
    text: str

class UpdateAdvert(AbstractAdvert):
    title: Optional[str] = None
    text: Optional[str] = None
