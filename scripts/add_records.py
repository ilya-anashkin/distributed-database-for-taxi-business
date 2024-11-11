import inspect

# from models import *

from config import Base, session
from models_provider import all_models

def __add_fake_records_for_model(model_cls):
    for _ in range(10):
        fake_instance = model_cls.fake()
        session.add(fake_instance)

    session.commit()


def add_fake_records():
    print("📝 Adding fake records to all models...")

    session.begin()

    for model in all_models:
        print(f"🧬 Adding fake records to {model.__name__}...")
        __add_fake_records_for_model(model)

    session.close()

    print("✅ Fake data added successfully to all models!")

if __name__ == "__main__":
    add_fake_records()