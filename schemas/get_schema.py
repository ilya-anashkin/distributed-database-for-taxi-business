from pydantic import BaseModel


class GetSchema(BaseModel):
    table_name: str
    id: int
