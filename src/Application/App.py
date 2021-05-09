from src.Services.TodoService.TodoService import TodoService


class App:
    def __init__(self, service_params):
        self._api_service = TodoService(service_params)

    def todo_service(self) -> TodoService:
        return self._api_service
