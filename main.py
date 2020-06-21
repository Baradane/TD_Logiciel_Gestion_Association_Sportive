import sys
from model.database import DatabaseEngine
from controller.person_controller import PersonController
from controller.sport_controller import SportController

from vue.root_frame import RootFrame


def main():


    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()

    person_controller = PersonController(database_engine)
    sport_controller = SportController(database_engine)

    root = RootFrame(person_controller, sport_controller)
    root.master.title("Association des sports")
    root.show_menu()

    root.mainloop()

if __name__ == "__main__":
    main()
