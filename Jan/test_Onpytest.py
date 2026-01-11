import pytest


@pytest.fixture
def myfixture_setup():
    print("...........print info about fixture")

def test_one(myfixture_setup):
    print("testOne ... ")

def test_two():
    print("testtwo... ")

def test_three(myfixture_setup):
    print("testthree ... ")