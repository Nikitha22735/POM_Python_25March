import pytest

@pytest.fixture(scope="session", autouse=True)
def precondition():
    print("im in session")

@pytest.fixture(scope="function")
def precondition_2():
    print("Im in function")

# @pytest.mark.results
def test_firstMethods(precondition_2):
    print("First testcase")

# @pytest.mark.results
def test_SecondMethods(precondition_2):
    print("test_SecondMethods")

