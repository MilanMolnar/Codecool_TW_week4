import ui
import log
import data_manager
import common





def create_app(table,file_name,main_list):
    log.logger.debug("Starting create_app function from application.py")
    def add_app(table, res_table):

        inputs = []
        inputs.append(common.generate_random(table))
        for i in range(0, len(res_table)):
            inputs.append(res_table[i])
        table.append(inputs)
        file1 = data_manager.get_table_from_file("Position/position.csv")
        file2 = data_manager.get_table_from_file("Student/student.csv")
        if common.is_in_table(file1, inputs[-1]) is False and common.is_in_table(file2, inputs[-2]) is False:
            return table
        else:
            raise ValueError

    table = add_app(table, ui.get_inputs(main_list, "Please provide the following information:"))

    data_manager.write_table_to_file(file_name, table)




def update_app(table, id_, accepted):
    log.logger.debug("Starting update_app function from application.py")
    for list in range(len(table)):
        for item in table[list]:
            if item in id_:
                table[list][1] = accepted
    ui.print_line("ID successfully updated!")
    return table



def remove_app(table, id_):
    log.logger.debug("Starting remove_app function from application.py")
    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    ui.print_line("ID successfully deleted!")
    return table



def start_module():
    log.logger.debug("Starting start_module function from application.py")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

            
            
def choose(menu):
    log.logger.debug("Starting choose function from application.py")
    file_name = "Application/application.csv"
    table = data_manager.get_table_from_file(file_name)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Accepted_field(yes[1] or no[0]): ","StudentID: ","PositionID: "]
    accepted =["Accepted? Yes[1] - No[0]: "]
    get_id = ["ID: "]
    if option == "1":
        try:
            create_app(table,file_name,main_list)
        except ValueError:
            ui.print_error_message("Student ID or Position ID do not exist!")
            start_module()
    elif option == "2":
        id_given = ui.get_inputs(get_id, "Please provide the following informations: ")
        accepted_given = ui.get_inputs(accepted, "")
        update_app(table, id_given, accepted_given[0])
        data_manager.write_table_to_file(file_name, table)

    elif option == "3":
        id_remove = ui.get_inputs(get_id, "Please provide the following information: ")
        remove_app(table, id_remove)
        data_manager.write_table_to_file(file_name, table)
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True



def handle_menu():
    log.logger.debug("Starting handle_menu function from application.py")
    options = ["Create application", "Update application", "Delete  application"]

    ui.print_menu("Application manager", options, "Back to main menu")
