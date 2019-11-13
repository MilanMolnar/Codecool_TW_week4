import ui
import random
import log



def generate_random(table):
    log.logger.debug("Starting generate_random function from common.py")
    generated = ''
    upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_chrs = ["+", "!", "%", "/", "=", "(", ")", "|", "<", ">", "#", "&", "@", "{", "}", "*"]
    word = [1, 2, 3, 4, 5, 6, 7, 8]
    while len(generated) != 8:
        generated = ''
        while len(word) != 0:
            random.shuffle(word)
            n = word[0]
            if n == 1 or n == 2:
                l=upper_case[random.randint(0, len(upper_case)-1)]
                generated += l
            if n == 3 or n == 4:
                l=lower_case[random.randint(0, len(lower_case)-1)]
                generated += l
            if n == 5 or n == 6:
                l=str(numbers[random.randint(0, len(numbers)-1)])
                generated += l
            if n == 7 or n == 8:
                l=special_chrs[random.randint(0, len(special_chrs)-1)]
                generated += l
            word.remove(word[0])
        if generated not in table:
            return generated
        else:
            continue
    return generated



def add(table, input_list):
    log.logger.debug("Starting add function from common.py")
    list = []
    list.append(generate_random(table))
    for i in range(1, len(input_list)):
        list.append(input_list[i])
    table.append(list)
    return table



def update(table, id_, new_list):
    log.logger.debug("Starting update function from common.py")
    for list in range(len(table)):
        for item in table[list]:
            if item in id_:
                for i in range(1,len(table[list])):
                    table[list][i] = new_list[i]
    return table



def remove(table, id_):
    log.logger.debug("Starting remove function from common.py")
    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    return table



def show_table(title_list, table):
    log.logger.debug("Starting show_table function from common.py")
    ui.print_table(table, title_list)

    
    
def sorting(list):
    log.logger.debug("Starting sorting function from common.py")
    sorted = False
    while sorted == False:
        sorted = True
        for obj in range(len(list) - 1):
            if list[obj] > list[obj + 1]:
                temp = list[obj]
                list[obj] = list[obj + 1]
                list[obj + 1] = temp
                sorted = False
    return list



def is_in_table(table, ID): #returns true/false
    log.logger.debug("Starting is_in_table function from common.py")
    for line in table:
        for item in line:
            if item in ID:
                return False
    return True
