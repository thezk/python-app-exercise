from sys import stderr
from src.Services.parse_todos import parse_todos

from src.Services.download_todos import download_todos
from src.Services.save_todos import save_todos


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)
        todos_url = "https://jsonplaceholder.typicode.com/todos/"
        order = ['id', 'userId', 'title', 'completed']
        folder_path = 'storage/'
        raw_todos = download_todos(todos_url)
        csv_todos = parse_todos(raw_todos, order)
        save_todos(csv_todos, folder_path)
        # TODO: follow README.md instructions
