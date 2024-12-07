import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from faker import Faker
from enum import Enum

load_dotenv(override=True)

DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "postgres")


class NodeType(Enum):
    MASTER = "5432"
    REPLICA1 = "5433"
    REPLICA2 = "5434"

current_node_type = next((node for node in NodeType if node.value == DB_PORT), None)

engine = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)
Session = sessionmaker(bind=engine)
session = Session()

engine_master = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{NodeType.MASTER.value}/{DB_NAME}"
)
engine_replica1 = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{NodeType.REPLICA1.value}/{DB_NAME}"
)
engine_replica2 = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{NodeType.REPLICA2.value}/{DB_NAME}"
)

__session_master = sessionmaker(bind=engine_master)()
__session_replica1 = sessionmaker(bind=engine_replica1)()
__session_replica2 = sessionmaker(bind=engine_replica2)()

sessions = {
	'master': __session_master,
	'replica1': __session_replica1,
	'replica2': __session_replica2
}

Base = declarative_base()

fake = Faker()
