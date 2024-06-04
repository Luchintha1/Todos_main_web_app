# Creating a method
def get_todos(filePath="todos.txt"):

    """ Read the text file and return a list """

    with open(filePath, 'r') as read_file:
        todo_list_local = read_file.readlines()
    return todo_list_local
a

def set_todos(todos_arg, filePath="todos.txt"):

    """ Write the text file and add todos to the list """

    with open(filePath, 'w') as write_file:
        write_file.writelines(todos_arg)