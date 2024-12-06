from fastapi import APIRouter, HTTPException
from core.table_manager import TableManager
from schemas.insert_schema import InsertSchema
from schemas.update_schema import UpdateSchema
from schemas.get_schema import GetSchema, GetAllSchema

router = APIRouter()


@router.post("/insert")
async def insert(schema: InsertSchema):
    try:
        TableManager.insert(schema)

        return {"message": "Record inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/update")
async def update(schema: UpdateSchema):
    try:
        TableManager.update(schema)

        return {"message": "Record updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get")
async def get(table_name: str, id: int, db_id: str):
    schema = GetSchema(table_name=table_name, id=id, db_id=db_id)
    try:
        record = TableManager.get(schema)

        return {"record": record}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/get_all")
async def get(table_name: str, db_id: str):
    schema = GetAllSchema(table_name=table_name, db_id=db_id)
    try:
        record = TableManager.get_all(schema)

        return record
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete")
async def delete(schema: GetSchema):
    try:
        TableManager.delete(schema)

        return {"message": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete_all")
async def delete_all(schema: GetAllSchema):
    try:
        TableManager.delete_all(schema)

        return {"message": "All records deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
