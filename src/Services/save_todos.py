from datetime import date

def save_todos(csv_todos, storage_path):
    for todo in csv_todos:
        save_todo(todo, storage_path)


def save_todo(todo, storage_path):
    filename = __generate_filename(todo, storage_path)
    with open(filename, 'w') as file:
        file.write(todo)


def __generate_filename(todo: str, storage_path):
    id = todo.split(',')[0]
    date_str = date.today().strftime("%Y_%m_%d")
    return f"{storage_path}{date_str}_{id}.csv"

    