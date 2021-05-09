from sys import stderr

from src.Services.TodoService.parse_todos import parse_todos
from src.Services.TodoService.download_todos import download_todos
from src.Services.TodoService.save_todos import save_todos


class TodoService:

    def __init__(self, params):
        self.__params = params


    def run(self):
        print('Running TodoService', file=stderr)
        raw_todos = download_todos(self.__params['todos_url'])
        csv_todos = parse_todos(raw_todos, self.__params['field_order'], self.__params['folder_path'])
        save_todos(csv_todos)
