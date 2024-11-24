from helpers.create_tables import create_tables
from helpers.delete_tables import delete_tables
from helpers.add_records import add_fake_records


def __run():
    delete_tables()
    create_tables()
    add_fake_records()

if __name__ == "__main__":
    __run()
