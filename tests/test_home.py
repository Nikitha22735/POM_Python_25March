from playwright.sync_api import sync_playwright, expect
import pytest
from pages.home import homePage

# pip install pytest-xdist

        
@pytest.mark.test12
def test_valiatingTheUIOfHomeScreen(page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)
        homePageObj.validateTheVisibilityOfSearchBar()
        homePageObj.validateAccountsNdListVisibility()       
        

@pytest.mark.test1
def test_ValidatingCartVisibility(page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)

        homePageObj.validateTheVisibilityOfSearchBar()
        expect(page.locator("#nav-cart-text-container")).to_be_visible()


@pytest.mark.test1
def test_ValidatingCartVisibility_1(page):
        homePageObj = homePage(page)
        
        page.goto("https://www.amazon.in/")
        homePageObj.validateTheVisibilityOfSearchBar()
        expect(page.locator("#nav-cart-text-container")).to_be_visible()



@pytest.mark.test1
def test_ValidatingCartVisibility_2(page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)
        homePageObj.validateTheVisibilityOfSearchBar()
        expect(page.locator("#nav-cart-text-container")).to_be_visible()




@pytest.mark.test1
def test_ValidatingCartVisibility_3(page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)
        homePageObj.validateTheVisibilityOfSearchBar()
        homePageObj.validateTheVisibilityOfCarticon()

# loc =  page.locator("input#twotabsearchtextbox")
def test_iphoneSearch(page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)
        homePageObj.enterSearchText('iphone')

def test_SamsungSearch(page):
        page.goto("https://www.amazon.in/")
        homePageObj = homePage(page)
        homePageObj.enterSearchText('Samsung')
        

        


