import log
import sys
import ui
from Application import application
from Company import company
from Position import position
from Student import student
log.logger.info("Main module")
def choose():
    log.logger.debug("main choosing menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        student.start_module()
    elif option == "2":
        company.start_module()
    elif option == "3":
        position.start_module()
    elif option == "4":
        application.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    log.logger.debug("main menupoints")
    options = ["Student",
               "Company",
               "Position",
               "Application"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    log.logger.debug("main menu starts")
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()