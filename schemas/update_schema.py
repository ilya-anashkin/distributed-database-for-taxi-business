from pydantic import BaseModel

class UpdateSchema(BaseModel):
	table_name: str
	columns: dict
