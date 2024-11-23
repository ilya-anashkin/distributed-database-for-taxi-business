from typing import Type, Any
from core.config import session
from schemas.insert_schema import InsertSchema
from schemas.update_schema import UpdateSchema
from schemas.get_schema import GetSchema

class TableManager:
    @staticmethod
    def insert(model: InsertSchema):
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        record = model_cls(model.columns)
        session.add(record)
        session.commit()

    @staticmethod
    def update(model: UpdateSchema):
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        record = session.query(model_cls).filter_by(id=model.id).first()
        if not record:
            raise ValueError(f"Record with id {model.id} not found")

        for key, value in model.columns.items():
            setattr(record, key, value)

        session.commit()

    @staticmethod
    def get(model: GetSchema) -> Any:
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        record = session.query(model_cls).filter_by(id=model.id).first()

        if not record:
            raise ValueError(f"Record with id {model.id} not found in table {model.table_name}")

        return record

    @staticmethod
    def __get_model_cls(table_name: str) -> Type:
        model_cls_name = table_name + 'Model'
        model_cls = globals().get(model_cls_name)
        if model_cls:
            return model_cls
        else:
            raise ValueError(f"Model class {model_cls_name} not found")