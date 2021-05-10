from sys import stderr

from src.Services.TodoService.parse_todos import parse_todos
from src.Services.TodoService.download_todos import download_todos
from src.Services.TodoService.save_todos import save_todos


class TodoService:

    def __init__(self, params: dict):
        self.__params = params


    def run(self):
        print('Running TodoService', file=stderr)
        raw_todos = download_todos(self.__params['TODOS_URL'])
        csv_todos = parse_todos(raw_todos, self.__params['FIELD_ORDER'], self.__params['STORAGE_FOLDER_PATH'])
        save_todos(csv_todos)
        print('TodoService executed successfully', file=stderr)
