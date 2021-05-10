from datetime import date


def parse_todos(raw_todos: list, ordered_fields: list, storage_path: str) -> list:
    return [
        {   
            'content': __json_to_csv(raw_todo, ordered_fields),
            'filename': __generate_filename(raw_todo, storage_path)
        } 
        for raw_todo in raw_todos]


def __json_to_csv(raw_todo: dict, ordered_fields: list) -> str:
    # The ordered field list gives us a consistent csv saving that doesn't depend on the dictionary iteration.
    values = [__stringify_value(raw_todo[field]) for field in ordered_fields]
    return ','.join(values)


def __stringify_value(value) -> str:
    str_value = str(value) or '' # default to empty value
    if ',' in str_value:
        str_value = f'"{str_value}"' # Adding the "" to escape the separator value in the CSV format if needed.
    return str_value


def __generate_filename(todo: dict, storage_path: str) -> str:
    date_str = date.today().strftime("%Y_%m_%d")
    return f"{storage_path}{date_str}_{todo['id']}.csv"