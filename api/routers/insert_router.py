from fastapi import APIRouter, HTTPException
from core.table_manager import TableManager
from schemas.insert_schema import InsertSchema

router = APIRouter()

@router.post()
async def insert(schema: InsertSchema):
	try:
		TableManager.create_table(schema.columns)

		return {"message": "Table created successfully"}
	except Exception as e:
		raise HTTPException(status_code=400, detail=str(e))