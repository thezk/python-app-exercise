

def save_todos(csv_todos: list):
    for todo in csv_todos:
        __save_todo(todo)


def __save_todo(todo: dict):
    with open(todo['filename'], 'w') as file:
        file.write(todo['content'])


