import allure
import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.home import homePage
from pages.login import loginPage
from pages.results import resultsPage
from pages.shopping_cart import shoppingCartPage


@pytest.fixture()
def homePageObj(page: Page):
    homePageObj_fixture = homePage(page)
    return homePageObj_fixture

@pytest.fixture()
def resultsPageObj(page: Page):
    resultsPageObj_f = resultsPage(page)
    return resultsPageObj_f

@pytest.fixture()
def loginPageObj(page: Page):
    loginpageObj_f = loginPage(page)
    return loginpageObj_f

@pytest.fixture()
def shoppingCartObj(page: Page):
    shoppingCartObj_f = shoppingCartPage(page)
    return shoppingCartObj_f

@pytest.fixture(scope="function")
def launchingAmazon(page: Page):
    page.goto("https://www.amazon.in/")
    continue_btn = page.get_by_role(
        "button",
        name="Continue shopping"
    )

    if continue_btn.is_visible(timeout=5000):
        continue_btn.click()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots for setup, call, and teardown failures
    if report.failed:
        page = item.funcargs.get("page", None)
        if page:
            step = report.when  # setup / call / teardown
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot ({step})",
                attachment_type=allure.attachment_type.PNG
            )

