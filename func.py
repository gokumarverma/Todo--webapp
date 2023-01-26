"""Variables declared"""
FILEPATH = 'Todo.txt'


def read(filepath=FILEPATH):
    """This function will read the text file and return a list of items"""
    with open(filepath, 'r') as file:
        todo_ = file.readlines()
    return todo_


def write(items, filepath=FILEPATH,):
    """This function will write a list to text file, it will not return anything"""
    with open(filepath, 'w') as file:
        file.writelines(items)
