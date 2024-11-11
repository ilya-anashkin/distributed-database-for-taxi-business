from delete_tables import delete_tables
from create_tables import create_tables
from add_records import add_fake_records

def __run():
    delete_tables()
    create_tables()
    add_fake_records()

if __name__ == "__main__":
    __run()
