from playwright.sync_api import sync_playwright
from pages.home import homePage
from pages.login import loginPage
from pages.results import resultsPage
from pages.shopping_cart import shoppingCartPage
from utils.jsonhandling import jsonFile
filepath = "testData/credentials.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    homePageObj = homePage(page)
    loginPageObj = loginPage(page)
    homePageObj.clickOnAccountsNdList()
    formattedData = jsonFile(filepath)
    loginPageObj.enterEmail(formattedData["positiveCredentials"]["username"])
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw(formattedData["positiveCredentials"]["password"])
    loginPageObj.clickOnSignBtn()
    page.wait_for_timeout(3000)
    context.storage_state(path="auth.json")
