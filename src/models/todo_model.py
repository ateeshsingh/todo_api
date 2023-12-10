from typing import Optional, Any
from pydantic import BaseModel, Field, field_serializer
from datetime import datetime
from bson import ObjectId


class TodosCreate(BaseModel):
    name: str
    description: str
    deadline: datetime
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    email:Optional[str] = None

class TodosUpdate(BaseModel):
    model_config = {
        "arbitrary_types_allowed": True
    }
    id: Any = Field(default=None, alias="_id", serialization_alias="id")
    name: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    email: Optional[str] = None

    @field_serializer('id')
    def serialize_dt(self, id: Any, _info):
        return str(id)
