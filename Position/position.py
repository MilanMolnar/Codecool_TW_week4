import ui
import log
import common
import data_manager
import main



def create_pos(table,file_name,main_list):
    log.logger.debug("Starting create_pos function from position.py")
    def add_pos(table, res_table):
        inputs = []
        inputs.append(common.generate_random(table))
        for i in range(0, len(res_table)):
            inputs.append(res_table[i])
        table.append(inputs)

        if int(inputs[2]) < 1:
            raise ValueError
        file = data_manager.get_table_from_file("Company/company.csv")
        if common.is_in_table(file, inputs[-1]) is False:
            return table
        else:
            ui.print_error_message("Company ID does not exist!")



    table = add_pos(table, ui.get_inputs(main_list, "Please provide the following information:"))

    data_manager.write_table_to_file(file_name, table)


    
def read_pos(table, ID):
    log.logger.debug("Starting read_pos function from position.py")
    for i in range(len(table)):
        if table[i][0] in ID:
            ui.print_line(table[i])
    # + students already applied are shown here
    ui.print_line("Student IDs already applied:")
    file = data_manager.get_table_from_file("Application/application.csv")
    for i in range(len(file)):
        if file[i][-1] in ID:
            ui.print_line(file[i][-2])
        elif file[i][-1] in ID:
            ui.print_line("There are no students applied right now.")

            
            
def read_positions(table):
    '''
    We print out all the positions, then we print out the position IDs, are in the application csv,
    which means somebody applied to that position.

    We print out the IDs that are not even in the application csv that means nobody applied for that position.

    If the position got applies and the company accepted them(1),
     we print out how many seats are taken in that position.

    If the position got applies but the company said no to them(0),
    we just print out "all seats are available" just like if it is not in the application csv.

    '''

    seat_list=[]
    seat_list_count=[]
    log.logger.debug("Starting read_positions function from position.py")
    file = data_manager.get_table_from_file("Application/application.csv")


    ui.print_line("Existing positions:\n /ID,Description,Seats,Company ID/\n")
    for sublist in table:
        ui.print_line(sublist)
    ui.print_line("\n")


    ui.print_line("Seats for positions:")
    for sublist in table:
        for sublist2 in file:
            if sublist[0] == sublist2[-1]:
                if sublist2[1] == "0":
                    ui.print_line("ID:"+sublist[0]+" "+"All seats are available")
                elif sublist2[1] =="1":
                    seat_list.append(sublist[0])


    table_ids = []
    for i in range(len(file)):
        table_ids.append(file[i][-1])

    for i in range(len(table)):
        if table[i][0] not in table_ids:
            ui.print_line("ID:"+table[i][0]+" "+"All seats are available")


    duplicated_id=[]
    one_id=[]
    for i in range(len(seat_list)):
        seat_list_count.append(seat_list.count(seat_list[i]))

    for i in range(len(seat_list)):
        if seat_list.count(seat_list[i]) > 1:
            duplicated_id.append(str(seat_list[i])+"+"+str(seat_list.count(seat_list[i])))
        elif seat_list.count(seat_list[i]) == 1:
            one_id.append(str(seat_list[i])+"+"+str(seat_list.count(seat_list[i])))

    for word in one_id:
        ui.print_line("ID:" + word[0:word.index("+")] + " " + word[word.index("+")+1:]+" Seat is taken.")

    duplicated_id = list(dict.fromkeys(duplicated_id))
    duplicated_id = list(dict.fromkeys(duplicated_id))


    for word in duplicated_id:
        ui.print_line("ID:" + word[0:word.index("+")] + " " + word[word.index("+")+1:]+" Seats are taken.")

    ui.print_line("\n")



def update_desc(table, id_, new_desc):
    log.logger.debug("Starting update_desc function from position.py")
    for list in range(len(table)):
        for item in table[list]:
            if item in id_:
                table[list][1] = new_desc
    ui.print_line("ID successfully updated!")
    return table



def remove_desc(table, id_):
    log.logger.debug("Starting remove_desc function from position.py")
    file = data_manager.get_table_from_file("Application/application.csv")
    for sublist in file:
        if sublist[-1] == id_[0]:
            ui.print_line('ID can not be deleted!')
            exit()

    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    ui.print_line("ID successfully deleted!")
    return table



def start_module():
    log.logger.debug("Starting start_module function from position.py")
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

            
            
def choose(menu):
    log.logger.debug("Starting choose function from position.py")
    file_name = "Position/position.csv"
    table = data_manager.get_table_from_file(file_name)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Description: ", "Seats: ", "Company_ID: "]
    description = ["Description: "]
    get_id = ["ID: "]
    if option == "1":
        try:
            create_pos(table, file_name, main_list)
        except ValueError:
            ui.print_line("Seat must be greater than 0!")
            start_module()
    elif option == "2":
        id_given = ui.get_inputs(get_id,"Please provide the following information:")
        read_pos(table,id_given)
    elif option == "3":
        read_positions(table)
    elif option == "4":
        id_given = ui.get_inputs(get_id,"Please provide the following informations: ")
        update_given = ui.get_inputs(description,"")
        update_desc(table,id_given,update_given[0])
        data_manager.write_table_to_file(file_name,table)
    elif option == "5":
        id_remove = ui.get_inputs(get_id,"Please provide the following information: ")
        remove_desc(table,id_remove)
        data_manager.write_table_to_file(file_name,table)
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True



def handle_menu():
    log.logger.debug("Starting handle_menu function from position.py")
    options = ["Create position", "Read position","Read positions", "Update position", "Delete position"]
    ui.print_menu("Position manager", options, "Back to main menu")
