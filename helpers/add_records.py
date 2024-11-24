import inspect

from core.config import Base, session, NodeType, current_node_type
from core.models_provider import all_models, ReplicationType


def __add_fake_records_for_model(model_cls):
    for i in range(1, 11):
        fake_instance = model_cls.fake(i)
        session.add(fake_instance)

    session.commit()


def add_fake_records():
    print("📝 Adding fake records to all models...")

    session.begin()

    for model, replication_type in all_models:
        if (
            replication_type == ReplicationType.WITH_MAIN_COPY
            or (replication_type == ReplicationType.WITHOUT_MAIN_COPY and model.__tablename__ != "unsatisfactory_rides")
        ) and (
            current_node_type == NodeType.REPLICA1
            or current_node_type == NodeType.REPLICA2
        ):
            continue
        if (
            replication_type == ReplicationType.COSOLIDATION
            and current_node_type == NodeType.MASTER
        ):
            continue

        if (
            model.__tablename__ == "unsatisfactory_rides"
            and current_node_type == NodeType.MASTER
        ):
            continue

        print(
            f"🧬 Adding fake records to {model.__name__} for {current_node_type.value}..."
        )
        __add_fake_records_for_model(model)

    session.close()

    print("✅ Fake data added successfully to all models!")


if __name__ == "__main__":
    add_fake_records()
