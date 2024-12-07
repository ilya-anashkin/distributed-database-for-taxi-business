from typing import Type, Any
from core.config import sessions
from schemas.insert_schema import InsertSchema
from schemas.update_schema import UpdateSchema
from schemas.get_schema import GetSchema, GetAllSchema

from models import *


class TableManager:
    @staticmethod
    def insert(model: InsertSchema):
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        record = model_cls(**model.columns)
        session = sessions.get(model.db_id)
        session.add(record)
        session.commit()

    @staticmethod
    def update(model: UpdateSchema):
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        session = sessions.get(model.db_id)
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

        session = sessions.get(model.db_id)
        record = session.query(model_cls).filter_by(id=model.id).first()

        if not record:
            raise ValueError(
                f"Record with id {model.id} not found in table {model.table_name}"
            )

        return record

    @staticmethod
    def get_all(model: GetAllSchema) -> Any:
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        session = sessions.get(model.db_id)
        record = session.query(model_cls).all()

        print(record, 555)

        if not record:
            raise ValueError(
                f"Record with id {model} not found in table {model.table_name}"
            )

        return record

    @staticmethod
    def delete(model: GetSchema):
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        session = sessions.get(model.db_id)
        record = session.query(model_cls).filter_by(id=model.id).first()
        if not record:
            raise ValueError(f"Record with id {model.id} not found")

        session.delete(record)
        session.commit()

    @staticmethod
    def delete_all(model: GetAllSchema):
        try:
            model_cls = TableManager.__get_model_cls(model.table_name)
        except ValueError as e:
            raise e

        session = sessions.get(model.db_id)
        record = session.query(model_cls).all()
        if not record:
            raise ValueError(f"Record with id {model.id} not found")

        for rec in record:
            session.delete(rec)
        session.commit()

    @staticmethod
    def __get_model_cls(table_name: str) -> Type:
        model_cls_name = ''.join(word.capitalize() for word in table_name.split('_')) + "Model"
        model_cls = globals().get(model_cls_name)
        if model_cls:
            return model_cls
        else:
            raise ValueError(f"Model class {model_cls_name} not found")
