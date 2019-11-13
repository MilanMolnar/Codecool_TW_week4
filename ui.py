import log




def print_table(table, title_list):
    log.logger.debug("Starting print_table function from ui.py")
    list_of_column_len = []
    list_of_title_leng = []
    list_of_width = []
    temp = []

    for j in range(len(title_list)):
        list_of_title_leng.append(len(title_list[j]))

    for i in range(len(table[0])):
        for j in range(len(table)):
            temp.append(float(len(table[j][i])))
        list_of_column_len.append(max(temp))
        temp = []

    for i in range(len(list_of_title_leng)):
        if list_of_column_len[i] >= list_of_title_leng[i]:
            list_of_width.append(list_of_column_len[i])
        else:
            list_of_width.append(list_of_title_leng[i])
    i = 0
    j = 0
    betw_line = ""
    betw_line += "╠"
    top_line = ""
    bottom_line = ""
    top_line += "╔"
    bottom_line += "╚"
    for leng in list_of_width:
        top_line += "═" * (int(leng) + 2) + "╦"
    for leng in list_of_width:
        betw_line += "═" * (int(leng) + 2) + "╬"
    for leng in list_of_width:
        bottom_line += "═" * (int(leng) + 2) + "╩"
    print(top_line[:-1] + "╗")
    print("║", end="")
    n = 0
    for item in title_list:
        if n <= len(title_list) - 2:
            print(" ", end="")
            print('{0:^{1}}'.format(item, int(list_of_width[n])) + " ║", end="")
        else:
            print(" ", end="")
            print('{0:^{1}}'.format(item, int(list_of_width[n])) + " ║")
        n += 1
    print(betw_line[:-1] + "╣")
    for list in table:
        print("║", end="")
        for item in list:
            print(" ", end="")
            print('{0:^{1}}'.format(item, int(list_of_width[i])) + " ║", end="")
            i += 1
        j += 1
        print()
        if j < len(table):
            print(betw_line[:-1] + "╣")
        i = 0
    print(bottom_line[:-1] + "╝")
    print()

def print_result(result, label):
    log.logger.debug("Starting print_result function from ui.py")
    print(label, result)

def print_menu(title, list_options, exit_message):
    log.logger.debug("Starting print_menu function from ui.py")
    print(title)
    for option in range(len(list_options)):
        print("   (" + str(option + 1) + ")", list_options[option] )
    print("   (0) " + exit_message)

def get_inputs(list_labels, title):
    log.logger.debug("Starting get_inputs function from ui.py")
    inputs = []
    print(title)
    for input_num in range(len(list_labels)):
        inputs.append(input(list_labels[input_num]))
    return inputs

def print_error_message(message):
    log.logger.debug("Starting print_error_message function from ui.py")
    print("ERROR:", message)

def print_line(line):
    log.logger.debug("Starting print_line function from ui.py")
    print(line)
