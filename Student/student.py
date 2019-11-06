import ui
import log
import data_manager

def start_module():
    table = data_manager.get_table_from_file("student.csv")
    log.logger.debug("student staring module")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

def choose(menu):
    log.logger.debug("student choosing option")
    file_name = "Student/student.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = [""]
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True


def handle_menu():
    log.logger.debug("student handling menu")
    options = ["Create student", "Read student", "Read students", "Update student","Change status", "Delete student"]

    ui.print_menu("Company manager", options, "Back to main menu")


