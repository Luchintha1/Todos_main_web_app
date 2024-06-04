# Creating a method
def get_todos(filePath="todos.txt"):

    """ Read the text file and return a list """
    try:
        with open(filePath, 'r') as read_file:
            todo_list_local = read_file.readlines()
    except:
        todo_list_local = []

    return todo_list_locala

def set_todos(todos_arg, filePath="todos.txt"):

    """ Write the text file and add todos to the list """

    with open(filePath, 'w') as write_file:
        write_file.writelines(todos_arg)