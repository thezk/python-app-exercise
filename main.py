#!/usr/bin/env python

from src.Application.App import App

"""
For good practices, the parameters for the app are set here.
Ideally, they would be set as an environment variable or another
external source.
"""

service_params = {
    "TODOS_URL": "https://jsonplaceholder.typicode.com/todos/",
    "FIELD_ORDER": ['id', 'userId', 'title', 'completed'],
    "STORAGE_FOLDER_PATH": 'storage/'
}

app = App(service_params)

app.todo_service().run()
