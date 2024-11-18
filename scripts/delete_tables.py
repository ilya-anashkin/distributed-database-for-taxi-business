from sqlalchemy import create_engine
from core.config import engine

from models_provider import all_models

def delete_tables():
    """
    Delete tables in the database
    """
    print("🗑️ Deleting tables...")

    for model in all_models.__reversed__():
        print(f"🧹 Deleting table {model.__name__}...")
        try:
            model.__table__.drop(engine)
        except Exception as e:
            print(f"❌ Error deleting table {model.__name__}: {e}")

    print("✅ All tables deleted")

if __name__ == "__main__":
    delete_tables()