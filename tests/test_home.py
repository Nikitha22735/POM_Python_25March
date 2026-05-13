from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.home import homePage

# pip install pytest-xdist

        
@pytest.mark.test1234
def test_valiatingTheUIOfHomeScreen(page: Page, homePageObj, launchingAmazon):
        # page.goto("https://www.amazon.in/")
        # homePageObj = homePage(page)
        homePageObj.validateTheVisibilityOfSearchBar()
        homePageObj.validateAccountsNdListVisibility()       
        

@pytest.mark.test1234
def test_ValidatingCartVisibility(page: Page, launchingAmazon):
        # page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)

        homePageObj.validateTheVisibilityOfSearchBar()
        expect(page.locator("#nav-cart-text-container")).to_be_visible()





# @pytest.mark.test1
def test_ValidatingCartVisibility(page: Page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)
        homePageObj.validateTheVisibilityOfSearchBar()
        homePageObj.validateTheVisibilityOfCarticon()


        

        


