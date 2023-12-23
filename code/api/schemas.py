from typing import Optional
from uuid import UUID

import fastapi
import pydantic

import decorators


@decorators.as_form
class ArticleSchema(pydantic.BaseModel):
    name: str
    description: str
    author_id: int

    
class ArticleGetSchema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
    
    
class ArticleUpdateSchema(pydantic.BaseModel):
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
