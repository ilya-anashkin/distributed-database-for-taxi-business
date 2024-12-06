from pydantic import BaseModel


class InsertSchema(BaseModel):
    table_name: str
    columns: dict
    db_id: str
