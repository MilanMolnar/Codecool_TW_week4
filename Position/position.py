import ui
import log

def start_module():
    log.logger.debug("position starting module")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

def choose(menu):
    log.logger.debug("position choosing option")
    file_name = "Position/position.csv"
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
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True


def handle_menu():
    log.logger.debug("position handling menu")
    options = ["Create position", "Read positions", "Update position", "Delete position"]

    ui.print_menu("Position manager", options, "Back to main menu")