import ui
import log
import data_manager
import common

log.logger.info("Application module")



def create_app(table,file_name,main_list):
    #kell egy input(new_line_app), ami bekéri a következőket: "app ID", "Acepted field(0/1)", "Student ID", "PosID"
    #uj lista (ID_checker) tartalma: "PosID", "StudentID"
    #ID_chackerrel végig kell iterálni az application és student.csv-n ID_chacker 0 vagy 1 eleme /
    #megegyezik-e a csv-k 0-dik elemével. ha igen akkor adja hozzá: new_line_app-ot
    #skeleton: if table[i][0] == ID_chacker[0] or table[i][0] == ID_chacker[1]
    #/if file[i][0] == ID_chacker[0] or file[i][0] == ID_chacker[1]
    #file referancing pos.csv, table ref student.csv
    pass


    log.logger.debug("application creating application")

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
            ui.print_error_message("Student ID or Position ID do not exist!")
            exit()

    table = add_app(table, ui.get_inputs(main_list, "Please provide the following information:"))

    data_manager.write_table_to_file(file_name, table)



def update_app(table, id_, accepted):
    log.logger.debug("application update accepted")
    for list in range(len(table)):
        for item in table[list]:
            if item in id_:
                table[list][1] = accepted
    ui.print_line("ID successfully updated!")
    return table


def remove_app(table, id_):
    log.logger.debug("application remove table")
    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    ui.print_line("ID successfully deleted!")
    return table


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
    table = data_manager.get_table_from_file(file_name)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = [""]
    accepted =["Accepted? Yes[1] - No[0]: "]
    get_id = ["ID: "]
    if option == "1":
        pass
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
    log.logger.debug("app handling menu")
    options = ["Create application", "Update application", "Delete  application"]

    ui.print_menu("Application manager", options, "Back to main menu")