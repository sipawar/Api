import configparser
from pathlib import Path

import pytest




# Define resources as a fixture if required (optional change for better integration)
@pytest.fixture(params=['/posts', '/comments', '/albums', '/photos', '/todos', '/users'])
def resource(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption("--get_task", action="store", default=None, help="Specify the task to run")

@pytest.fixture(scope='class',autouse=True)
def task(request):
    return request.config.getoption("--get_task")

@pytest.fixture(scope="class",autouse=True)
def read_ini():
    path = Path(__file__).resolve().parent.parent / 'pytest.ini'
    config = configparser.ConfigParser()
    config.read(path)
    return config

