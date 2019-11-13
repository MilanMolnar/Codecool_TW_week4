import ui
import log
import data_manager
import common
import data_manager


def read_student(table, ID):
    log.logger.debug("Starting read_student function from student.py")
    for i in range(len(table)):
        if table[i][0] in ID:
            ui.print_line(table[i])

            
            
def change_status(table, ID_input):
    log.logger.debug("Starting change_status function from student.py")
    for i in range(len(table)):
        if table[i][0] in ID_input:
            if table[i][-1] == '1':
                table[i][-1] = '0'
            else:
                table[i][-1] = '1'
    return table



def read_student(table, ID):
    log.logger.debug("Starting read_student function from student.py")

    file_app = data_manager.get_table_from_file("Application/application.csv")

    for i in range(len(table)):
        if table[i][0] in ID:
            ui.print_line("Student: " + str(table[i]))

    result = []
    for i in range(len(file_app)):
        if file_app[i][2] == ID[0]:
            result.append(file_app[i])
    if len(result) == 0:
        ui.print_line("No application for the student!")
    elif len(result) == 1:
        ui.print_line("Application: " + str(result[0]))
    else:
        ui.print_line("Applications: " + str(result))

        
        
def remove_student(table, id_):
    log.logger.debug("Starting remove_student function from student.py")

    file = data_manager.get_table_from_file("Application/application.csv")
    for sublist in file:
        if sublist[2] == id_[0]:
            ui.print_line('ID can not be deleted!')
            raise ValueError

    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    ui.print_line("ID successfully deleted!")
    return table



def start_module():
    log.logger.debug("Starting start_module function from student.py")
    table = data_manager.get_table_from_file("Student/student.csv")
    log.logger.debug("student staring module")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

            
            
def choose(menu):
    log.logger.debug("Starting choose function from student.py")
    file_name = "Student/student.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press enter to continue...", "Name: ", "Age: ", "Status(0/1): "]
    label = ["ID", "Name", "Age", "Status"]
    if option == "1":
        table = common.add(data_manager.get_table_from_file(file_name),
                    ui.get_inputs(main_list, "Please provide the following information:"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "2":
        table = data_manager.get_table_from_file(file_name)
        get_id = ["ID: "]
        id_given = ui.get_inputs(get_id, "Please provide the following information:")
        read_student(table, id_given)
    elif option == "3":
        common.show_table(label, data_manager.get_table_from_file(file_name))
    elif option == "4":
        table = common.update(data_manager.get_table_from_file(file_name),
                       ui.get_inputs(["ID: "], "Please provide the ID to identify the student:"),
                       ui.get_inputs(main_list, "Please provide the following information to complete the update"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        table = change_status(data_manager.get_table_from_file(file_name),
                      ui.get_inputs(["ID: "], "Please provide the ID to identify the student:"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "6":
        try:
            get_id = ["ID: "]
            table = data_manager.get_table_from_file(file_name)
            id_remove = ui.get_inputs(get_id, "Please provide the following information: ")
            remove_student(table, id_remove)
            data_manager.write_table_to_file(file_name, table)
        except ValueError:
            start_module()
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True



def handle_menu():
    log.logger.debug("Starting handle_menu function from student.py")
    options = ["Create student", "Read student", "Read students", "Update student","Change status", "Delete student"]
    ui.print_menu("Student manager", options, "Back to main menu")
