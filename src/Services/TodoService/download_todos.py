from requests import get


def download_todos(todos_url):
    return get(todos_url).json()
