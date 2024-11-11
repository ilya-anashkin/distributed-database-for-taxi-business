import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Параметры подключения из .env
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Базовая модель и подключение к базе
Base = declarative_base()
engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Session = sessionmaker(bind=engine)

class MyTable(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

class DatabaseService:
    def __init__(self):
        self.session = Session()

    def create_tables(self):
        """Создает все таблицы, определенные в модели Base"""
        Base.metadata.create_all(engine)
        print("Таблицы созданы")

    def close(self):
        """Закрывает сессию"""
        self.session.close()

# Пример использования
if __name__ == "__main__":
    db_service = DatabaseService()
    db_service.create_tables()
    db_service.close()