#!/usr/bin/env python

from src.Application.App import App


service_params = {
    "todos_url": "https://jsonplaceholder.typicode.com/todos/",
    "field_order": ['id', 'userId', 'title', 'completed'],
    "folder_path": 'storage/'
}

app = App(service_params)

app.todo_service().run()
