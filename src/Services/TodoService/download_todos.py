from requests import get


def download_todos(todos_url: str) -> dict:
    return get(todos_url).json()
