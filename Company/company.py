import ui
import log
import common
import data_manager


def start_module():
    log.logger.debug("Starting start_module function from company.py")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

            
            
def read_company(table, ID):
    log.logger.debug("Starting read_company function from company.py")
    file_pos = data_manager.get_table_from_file("Position/position.csv")

    for i in range(len(table)):
        if table[i][0] in ID:
            ui.print_line("Company: " + str(table[i]))

    result = []
    for i in range(len(file_pos)):
        if file_pos[i][3] == ID[0]:
            result.append(file_pos[i])

    if len(result) == 0:
        ui.print_line("There is no position for that company.")
    elif len(result) == 1:
        ui.print_line("Position: "+ str(result[0]))
    else:
        ui.print_line("Positions: "+ str(result))
      
    
    
def remove_company(table, id_):
    log.logger.debug("Starting remove_company function from company.py")
    file = data_manager.get_table_from_file("Position/position.csv")
    for sublist in file:
        if sublist[-1] == id_[0]:
            ui.print_line('ID can not be deleted!')
            raise ValueError

    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    ui.print_line("ID successfully deleted!")
    return table



def choose(menu):
    log.logger.debug("Starting choose function from company.py")
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
        table = data_manager.get_table_from_file(file_name)
        get_id = ["ID: "]
        id_given = ui.get_inputs(get_id,"Please provide the following information:")
        read_company(table, id_given)
    elif option == "3":
        common.show_table(label, data_manager.get_table_from_file(file_name))
    elif option == "4":
        table = common.update(data_manager.get_table_from_file(file_name),
                              ui.get_inputs(["ID: "], "Please provide the ID to identify the company:"),
                              ui.get_inputs(main_list,
                                            "Please provide the following information to complete the update"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        try:
            get_id = ["ID: "]
            table = data_manager.get_table_from_file(file_name)
            id_remove = ui.get_inputs(get_id, "Please provide the following information: ")
            remove_company(table, id_remove)
            data_manager.write_table_to_file(file_name, table)
        except ValueError:
            start_module()
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True



def handle_menu():
    log.logger.debug("Starting handle_menu function from company.py")
    options = ["Create company", "Read company", "Read companies", "Update Company","Delete Company"]
    ui.print_menu("Company manager", options, "Back to main menu")
