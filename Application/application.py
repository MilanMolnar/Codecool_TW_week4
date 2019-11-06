import ui
import log




def start_module():
    log.logger.debug("app starting module")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

def choose(menu):
    log.logger.debug("app choosing option")
    file_name = "Application/application.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = [""]
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True


def handle_menu():
    log.logger.debug("app handling menu")
    options = ["Create application", "Update application", "Delete  application"]

    ui.print_menu("Application manager", options, "Back to main menu")