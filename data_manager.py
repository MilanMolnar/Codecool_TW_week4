import log

def get_table_from_csv(filename):
    log.logger.debug("data manager getting table from csv file")
    '''
    :param filename: Reads csv file
    :return: Lines are rows columns are separated by ";", we get list of lists
    '''
    with open(filename, "r") as file:
        lines = file.readlines()
    table =[element.replace("\n","").split(";") for element in lines]
    return table

def write_table_to_csv(filename,table):
    log.logger.debug("data manager write to csv")
    '''
    :param filename: write list of lists into a csv file
    :return: None
    '''
    with open(filename, "w") as file:
        for record in table:
            row = ";".join(record)
            file.write(row + "\n")