import ui
import log
import common
import data_manager



def create_pos(table,file_name,main_list):

    def add_pos(table, res_table):
        log.logger.debug("common adding to table")
        inputs = []
        inputs.append(common.generate_random(table))
        for i in range(0, len(res_table)):
            inputs.append(res_table[i])
        table.append(inputs)
        return table
    table = add_pos(table, ui.get_inputs(main_list, "Please provide the following information:"))

    file = data_manager.get_table_from_file("Company/company.csv")


    data_manager.write_table_to_file(file_name, table)





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
    table = data_manager.get_table_from_file(file_name)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Description: ", "Seats: ", "Company_ID: "]
    if option == "1":
        create_pos(table, file_name, main_list)
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