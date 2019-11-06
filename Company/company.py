import ui
import log
import common
import data_manager

def start_module():
    log.logger.debug("company starting module")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

def read_company(table, ID):
    for i in range(len(table)):
        if table[i][0] in ID:
            ui.print_line(table[i])


def choose(menu):
    log.logger.debug("company choosing option")
    file_name = "Company/company.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press enter to continue...", "Name: "]
    label = ["ID", "Name"]

    if option == "1":
        table = common.add(data_manager.get_table_from_file(file_name),
                           ui.get_inputs(main_list, "Please provide the following information:"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "2":
        read_company(data_manager.get_table_from_file(file_name),
                     ui.get_inputs(["ID: "], "Please provide the ID to identify the company:"))
    elif option == "3":
        common.show_table(label, data_manager.get_table_from_file(file_name))
    elif option == "4":
        table = common.update(data_manager.get_table_from_file(file_name),
                              ui.get_inputs(["ID: "], "Please provide the ID to identify the company:"),
                              ui.get_inputs(main_list,
                                            "Please provide the following information to complete the update"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        ID = ui.get_inputs(["ID: "], "Please provide the following information:")
        if common.is_in_table(data_manager.get_table_from_file("Position/position.csv"), ID):
            table = common.remove(data_manager.get_table_from_file(file_name), ID)
            data_manager.write_table_to_file(file_name, table)
        else:
            pass
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True


def handle_menu():
    log.logger.debug("company handling menu")
    options = ["Create company", "Read company", "Read companies", "Update Company","Delete Company"]

    ui.print_menu("Company manager", options, "Back to main menu")