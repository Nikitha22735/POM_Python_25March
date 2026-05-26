import allure
from playwright.sync_api import Page, expect



class homePage:
    def __init__(self, page):
        self.page = page
        
    # Self-Healing Locator Methods
    def get_search_bar(self):
        """Self-healing search bar locator with fallback strategies"""
        try:
            # Primary locator
            locator = self.page.locator("#twotabsearchtextbox")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 1: by name attribute
            locator = self.page.locator("input[name='keywords']")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 2: by placeholder
            locator = self.page.locator("input[placeholder*='Search']")
            if locator.is_visible():
                return locator
        except:
            pass
        
        # Last resort: return primary
        return self.page.locator("#twotabsearchtextbox")

    def get_accounts_nd_list_btn(self):
        """Self-healing accounts & lists button with fallback strategies"""
        try:
            # Primary locator
            locator = self.page.get_by_text("Account & Lists")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 1: by role
            locator = self.page.get_by_role("button", name="Account & Lists")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 2: by test id or data attribute
            locator = self.page.locator("[data-testid='account-lists-button']")
            if locator.is_visible():
                return locator
        except:
            pass
        
        # Last resort
        return self.page.get_by_text("Account & Lists")

    def get_cart_icon(self):
        """Self-healing cart icon locator with fallback strategies"""
        try:
            # Primary locator
            locator = self.page.locator("#nav-cart-text-container")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 1: by class
            locator = self.page.locator(".nav-cart-text-container")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 2: by aria-label
            locator = self.page.locator("[aria-label*='Cart']")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 3: by xpath pattern
            locator = self.page.locator("//span[contains(@id, 'cart')]")
            if locator.is_visible():
                return locator
        except:
            pass
        
        # Last resort
        return self.page.locator("#nav-cart-text-container")

    def get_search_btn(self):
        """Self-healing search button locator with fallback strategies"""
        try:
            # Primary locator
            locator = self.page.locator("#nav-search-submit-button")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 1: by role
            locator = self.page.get_by_role("button", name="Search")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 2: by class
            locator = self.page.locator("button.s-button")
            if locator.is_visible():
                return locator
        except:
            pass
        
        try:
            # Fallback 3: by type
            locator = self.page.locator("button[type='submit']").first
            if locator.is_visible():
                return locator
        except:
            pass
        
        # Last resort
        return self.page.locator("#nav-search-submit-button")

    @allure.step("validateTheVisibilityOfSearchBar")
    def validateTheVisibilityOfSearchBar(self):
        """Validate search bar visibility with self-healing"""
        self.get_search_bar().wait_for(state='visible')

    def validateAccountsNdListVisibility(self):
        """Validate accounts & lists button visibility with self-healing"""
        expect(self.get_accounts_nd_list_btn()).to_be_visible()

    def clickOnAccountsNdList(self):
        """Click accounts & lists button with self-healing"""
        self.get_accounts_nd_list_btn().click()

    def enterSearchText(self, product):
        """Enter search text with self-healing"""
        search_bar = self.get_search_bar()
        search_bar.wait_for(state='visible')
        search_bar.fill(product)

    def validateTheVisibilityOfCarticon(self):
        """Validate cart icon visibility with self-healing"""
        expect(self.get_cart_icon()).to_be_visible()

    def clickOnSearchBtn(self):
        """Click search button with self-healing"""
        self.get_search_btn().click()

