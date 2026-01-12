import  pytest


@pytest.fixture(scope="session")
def TC_setu():
    print("This is from conftest fixture")