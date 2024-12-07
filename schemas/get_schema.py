from pydantic import BaseModel


class GetSchema(BaseModel):
    table_name: str
    id: int
    db_id: str

class GetAllSchema(BaseModel):
    table_name: str
    db_id: str
