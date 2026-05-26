import allure
from playwright.sync_api import Page, expect



class homePage:
    def __init__(self,page):
        # Self-healing locators with multiple fallback strategies
        self.searchBar = page.locator("#twotabsearchtextbox").or_(page.locator("input[name='field-keywords']")).or_(page.locator("input[placeholder*='Search']"))
        self.accountsNdListBtn = page.get_by_text("Account & Lists").or_(page.locator("a[id*='nav-account']")).or_(page.locator("span:has-text('Account')"))
        self.cartIcon = page.locator("#nav-cart-text-container").or_(page.get_by_text("Cart")).or_(page.locator("[id*='cart']"))
        
        # Search button with error handling
        def searchBtn():
            try:
                self.searchBtn = page.locator("#nav-search-submit-button")
            except Exception as e:
                print(f"Error locating search button with primary locator: {str(e)}")
                try:
                    self.searchBtn = page.get_by_role("button", name="Go")
                except Exception as e:
                    print(f"Error locating search button with secondary locator: {str(e)}")
                    try:
                        self.searchBtn = page.locator("button[id*='search']")
                    except Exception as e:
                        print(f"Error locating search button with tertiary locator: {str(e)}")
                        self.searchBtn = None
    


    @allure.step("validateTheVisibilityOfSearchBar")
    def validateTheVisibilityOfSearchBar(self):
        self.searchBar.wait_for(state='visible')


    def validateAccountsNdListVisibility(self):
        expect(self.accountsNdListBtn).to_be_visible()

    def clickOnAccountsNdList(self):
        self.accountsNdListBtn.click()

    def enterSearchText(self, product):
        self.searchBar.wait_for(state='visible')
        self.searchBar.fill(product)

    def validateTheVisibilityOfCarticon(self):
        expect(self.cartIcon).to_be_visible()

    def clickOnSearchBtn(self):
        try:
            if self.searchBtn is not None:
                self.searchBtn.click()
            else:
                raise Exception("searchBtn locator is not initialized")
        except Exception as e:
            print(f"Error clicking search button: {str(e)}")
            raise

