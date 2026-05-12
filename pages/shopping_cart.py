from playwright.sync_api import Page, expect


class shoppingCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cartItems = page.locator('[data-component-type="s-search-result"]')
        self.productLink = lambda product_name: page.get_by_role("link", name=product_name, exact=True)
        self.proceedToCheckout = page.get_by_role("button", name="Proceed to checkout")
        self.itemInCart = page.get_by_role("link", name="item in cart")
    
    def verifyProductVisibleInCart(self, product_name):
        """Verify that a specific product is visible in the shopping cart"""
        expect(self.productLink(product_name)).to_be_visible()
    
    def getProductByName(self, product_name):
        """Get product element by name from cart"""
        return self.productLink(product_name)
    
    def clickOnItemInCart(self):
        """Click on an item in the cart"""
        self.itemInCart.click()
    
    def proceedToCheckoutClick(self):
        """Click Proceed to Checkout button"""
        self.proceedToCheckout.click()
