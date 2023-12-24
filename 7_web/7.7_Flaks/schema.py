from abc import ABC
from typing import Optional

import pydantic


class AbstractUser(pydantic.BaseModel, ABC):
    name: str
    password: str


    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError(f"Minimal length of password is 8")
        return v


class CreateUser(AbstractUser):
    name: str
    password: str

class UpdateUser(AbstractUser):
    name: Optional[str] = None
    password: Optional[str] = None


class AbstractAdvert(pydantic.BaseModel, ABC):
    # author_id: int
    title: str
    text: str

class CreateAdvert(AbstractAdvert):
    # author_id: int
    title: str
    text: str

class UpdateAdvert(AbstractAdvert):
    title: Optional[str] = None
    text: Optional[str] = None
