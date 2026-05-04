import pytest

from pages.home import homePage
from pages.results import resultsPage


@pytest.fixture()
def homePageObj(page):
    homePageObj_fixture = homePage(page)
    return homePageObj_fixture

@pytest.fixture()
def resultsPageObj(page):
    resultsPageObj_f = resultsPage(page)
    return resultsPageObj_f

@pytest.fixture(scope="function",autouse=True)
def launchingAmazon(page):
    page.goto("https://www.amazon.in/")

# @pytest.fixture()
# def logInToAmazon(page):

