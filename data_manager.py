import log

def get_table_from_file(filename):
    log.logger.debug("Starting get_table_from_file function from data_manager.py")
    
    '''
    :param filename: Reads csv file
    :return: Lines are rows columns are separated by ";", we get list of lists
    '''
    
    with open(filename, "r") as file:
        lines = file.readlines()
    table =[element.replace("\n","").split(";") for element in lines]
    return table



def write_table_to_file(filename,table):
    log.logger.debug("Starting write_table_to_file function from data_manager.py")
    
    '''
    :param filename: write list of lists into a csv file
    :return: None
    '''
    
    with open(filename, "w") as file:
        for record in table:
            row = ";".join(record)
            file.write(row + "\n")
