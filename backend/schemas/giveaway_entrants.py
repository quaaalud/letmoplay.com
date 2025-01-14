# -*- coding: utf-8 -*-

from pydantic import BaseModel, EmailStr


class EntrantCreate(BaseModel):
    email : EmailStr
    zip_code: str = None

class ShowEntrant(BaseModel):
    email : EmailStr

    class Config():
        from_attributes = True