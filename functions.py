FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        return file.readlines()


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write items from a list into a text file.
    """
    with open(filepath, 'w') as filename:
        filename.writelines(todos_arg)
