#!/usr/bin/env python

from src.Application.App import App


service_params = {
    "TODOS_URL": "https://jsonplaceholder.typicode.com/todos/",
    "FIELD_ORDER": ['id', 'userId', 'title', 'completed'],
    "STORAGE_FOLDER_PATH": 'storage/'
}

app = App(service_params)

app.todo_service().run()
