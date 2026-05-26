
import pytest


@pytest.fixture(scope="session")
def f1():
    print("inside f1")
    yield
    print("psot condition")


def test_f2(f1):
    print("im inside testcase")

def test_f3(f1):
    print("im inside testcase 1")