

def parse_todos(raw_todos, ordered_fields):
    return [__json_to_csv(raw_todo, ordered_fields) for raw_todo in raw_todos]


def __json_to_csv(raw_todo, ordered_fields):
    values = [str(raw_todo[field]) for field in ordered_fields]
    return ','.join(values)
    