import pytest
from faker import Faker


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://computer-database.gatling.io/computers",
                     help='help="Type the base URL: http://someurl.com. Default is https://computer-database.gatling.io/computers')


@pytest.fixture(scope='class')
def base_url(request):
    base_url = request.config.getoption("base_url")
    request.cls.base_url = base_url

    return base_url


@pytest.fixture(scope='session')
def faker():
    faker = Faker()
    # faker.random.seed(4321)
    return faker
