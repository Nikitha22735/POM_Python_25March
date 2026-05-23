import re
from playwright.sync_api import Page, expect
import json

import pytest
from utils.jsonhandling import jsonFile
filepath = "testData/credentials.json"

@pytest.mark.test1
def test_example(page: Page, homePageObj,loginPageObj) -> None:
    page.goto("https://www.amazon.in/")
    homePageObj.clickOnAccountsNdList()
    formattedData = jsonFile(filepath)
    loginPageObj.enterEmail(formattedData["positiveCredentials"]["username"])
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw(formattedData["positiveCredentials"]["password"])
    loginPageObj.clickOnSignBtn()
    page.wait_for_timeout(3000)
    homePageObj.validateTheVisibilityOfSearchBar()


def test_example_1(page_noAuth: Page, homePageObj,loginPageObj) -> None:
    page_noAuth.goto("https://www.amazon.in/")
    homePageObj.clickOnAccountsNdList()    
    formattedData = jsonFile(filepath)        
    loginPageObj.enterEmail("ttt")
    loginPageObj.clickOnContinueBtn()  
    loginPageObj.validateTheEmailError()

