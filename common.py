import ui
import random
import log

def generate_random(table):
    log.logger.debug("common generating random number")
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

def add(table, res_table):
    log.logger.debug("common adding to table")
    list = []
    list.append(generate_random(table))
    for i in range(1, len(res_table)):
        list.append(res_table[i])
    table.append(list)
    return table

def update(table, id_, new_list):
    log.logger.debug("common update table")
    for list in range(len(table)):
        for item in table[list]:
            if item in id_:
                for i in range(1,len(table[list])):
                    table[list][i] = new_list[i]
    return table

def remove(table, id_):
    log.logger.debug("common remove table")
    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    return table

def show_table(title_list, table):
    log.logger.debug("common show table")
    ui.print_table(table, title_list)

def sorting(list):
    log.logger.debug("common sorting...")
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