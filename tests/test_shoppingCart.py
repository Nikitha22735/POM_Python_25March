import pytest
import allure
from playwright.sync_api import expect, Page
from pages.login import loginPage
from pages.home import homePage
from pages.results import resultsPage
from pages.shopping_cart import shoppingCartPage


@allure.feature("Shopping Cart")
@allure.story("Add product to cart and verify")
def test_example(page: Page, loginPageObj: loginPage, homePageObj: homePage, 
                 resultsPageObj: resultsPage, shoppingCartObj: shoppingCartPage,launchingAmazon) -> None:
    """
    Test to search for an iPhone on Amazon, add it to cart, and verify it appears in the shopping cart
    """
    
    # Login to Amazon
    with allure.step("Login with credentials"):
        homePageObj.clickOnAccountsNdList()
        loginPageObj.enterEmail("trainingplaywright@gmail.com")
        loginPageObj.clickOnContinueBtn()
        loginPageObj.enterPw("Welcome@04")
        loginPageObj.clickOnSignBtn()
    
    # Search for iPhone
    with allure.step("Search for iPhone on Home page"):
        homePageObj.validateTheVisibilityOfSearchBar()
        homePageObj.enterSearchText("iphone")
        homePageObj.clickOnSearchBtn()
    
    # Click on first product and add to cart
    with allure.step("Select first product from search results"):
        resultsPageObj.clickOnFirstProduct()
    
    # Click on the product link to view details/add to cart
    with allure.step("Click on product in cart"):
        shoppingCartObj.clickOnItemInCart()
    
    # Verify product is visible in shopping cart
    with allure.step("Verify Apple iPhone product is visible in shopping cart"):
        expect(page.get_by_role("link", name="Apple iPhone Air 256 GB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Space Black", exact=True)).to_be_visible()
