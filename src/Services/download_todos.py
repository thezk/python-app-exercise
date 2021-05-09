from requests import get
from requests.exceptions import RequestException


def download_todos(todos_url):
    request = get(todos_url)
    return request.json()

