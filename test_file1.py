import pytest
# pip install pytest-order

# 1 2 3----   0   -10 -9----

def test_firstMethods():
    l1 =[1,2]
    print("first testcase")
    print(l1[2])

# @pytest.mark.skip
@pytest.mark.sample
@pytest.mark.regression
@pytest.mark.order(-3)
def test_SecondMethods():
    print("test_SecondMethods")

@pytest.mark.sample
@pytest.mark.order(-2)
def test_firstMethods_1():
    print("test_firstMethods_1")

@pytest.mark.regression
@pytest.mark.sample
@pytest.mark.order(1)
def test_firstMethods_2():  
    print("test_firstMethods_2")

@pytest.mark.skip
def test_firstMethods_3():
    print("first testcase skiping")