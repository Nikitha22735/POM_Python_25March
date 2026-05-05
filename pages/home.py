from playwright.sync_api import Page, expect


class homePage:

    def __init__(self,page:Page):
        self.searchBar = page.locator("#twotabsearchtextbox")
        self.accountsNdListBtn = page.get_by_text("Account & Lists")
        self.cartIcon = page.locator("#nav-cart-text-container")
        self.searchBtn = page.locator("#nav-search-submit-button")


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
        self.searchBtn.click()

