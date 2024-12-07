from pydantic import BaseModel


class UpdateSchema(BaseModel):
    table_name: str
    id: int
    columns: dict
    db_id: str
