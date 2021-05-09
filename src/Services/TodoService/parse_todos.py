from datetime import date


def parse_todos(raw_todos, ordered_fields, storage_path):
    return [
        {   
            'content': __json_to_csv(raw_todo, ordered_fields),
            'filename': __generate_filename(raw_todo, storage_path)
        } 
        for raw_todo in raw_todos]


def __json_to_csv(raw_todo, ordered_fields):
    values = [str(raw_todo[field]) for field in ordered_fields]
    return ','.join(values)


def __generate_filename(todo: dict, storage_path):
    date_str = date.today().strftime("%Y_%m_%d")
    return f"{storage_path}{date_str}_{todo['id']}.csv"