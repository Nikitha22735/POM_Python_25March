import pytest
import allure
from playwright.sync_api import Page, expect
from pages.home import homePage
from pages.results import resultsPage


@pytest.mark.searchResults
@allure.story("Search Results Verification")
def test_verifySearchResultsDisplayed(page: Page, homePageObj: homePage, resultsPageObj: resultsPage, launchingAmazon):
    with allure.step("Search for iPhone on home page"):
        homePageObj.enterSearchText("iphone")
        homePageObj.clickOnSearchBtn()
        page.wait_for_timeout(2000)
    
    with allure.step("Verify search results are displayed"):
        resultsPageObj.verifySearchResultsDisplayed()

    
    with allure.step("Verify products are displayed on page"):
        total_products = resultsPageObj.getTotalProductsOnPage()
        assert total_products > 0, "No products found on search results page"
        allure.attach(
            f"Total Products: {total_products}",
            name="Products Count",
            attachment_type=allure.attachment_type.TEXT
        )


