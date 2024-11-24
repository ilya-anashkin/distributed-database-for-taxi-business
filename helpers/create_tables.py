from core.config import engine, Base
import models

def create_tables():
    """
    Create tables in the database
    """
    print("🏗️ Creating tables...")

    Base.metadata.create_all(engine)

    print("✅ All tables created")

if __name__ == "__main__":
    create_tables()
