from fastapi import APIRouter, HTTPException
from core.table_manager import TableManager
from schemas.insert_schema import InsertSchema
from schemas.update_schema import UpdateSchema
from schemas.get_schema import GetSchema

router = APIRouter()

@router.post('/insert')
async def insert(schema: InsertSchema):
	try:
		TableManager.insert(schema)

		return {"message": "Record inserted successfully"}
	except Exception as e:
		raise HTTPException(status_code=400, detail=str(e))

@router.put('/update')
async def update(schema: UpdateSchema):
	try:
		TableManager.update(schema)

		return {"message": "Record updated successfully"}
	except Exception as e:
		raise HTTPException(status_code=400, detail=str(e))

@router.get('/get')
async def get(schema: GetSchema):
	try:
		record = TableManager.get(schema)

		return {"record": record}
	except Exception as e:
		raise HTTPException(status_code=400, detail=str(e))
