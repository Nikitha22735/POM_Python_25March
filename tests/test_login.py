import re
from playwright.sync_api import Page, expect
import json
from utils.jsonhandling import jsonFile
filepath = "testData/credentials.json"

def test_example(page: Page, homePageObj,loginPageObj) -> None:
    page.goto("https://www.amazon.in/")
    homePageObj.clickOnAccountsNdList()
    formattedData = jsonFile(filepath)
    loginPageObj.enterEmail(formattedData["positiveCredentials"]["username"])
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw(formattedData["positiveCredentials"]["password"])
    loginPageObj.clickOnSignBtn()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()


def test_example_1(page: Page, homePageObj,loginPageObj) -> None:
    page.goto("https://www.amazon.in/")
    homePageObj.clickOnAccountsNdList()    
    formattedData = jsonFile(filepath)        
    loginPageObj.enterEmail(formattedData["positiveCredentials"]["username"])
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw(formattedData["positiveCredentials"]["password"])
    loginPageObj.clickOnSignBtn()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()

