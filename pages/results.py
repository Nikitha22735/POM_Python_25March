
from playwright.sync_api import Page, expect
class resultsPage:
    def __init__(self, page:Page):
        # self.addToCartBtn = page.locator("(//span[contains(text(),'iPhone 17 Pro 256 GB')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        self.addToCartBtn = lambda product: page.locator(f"(//span[contains(text(),'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        self.cartCount = page.locator("#nav-cart-count")
       


    def addAnItmeToCart(self, itemName):
        self.addToCartBtn(itemName).click()


    def getCartCount(self):
        return self.cartCount.text_content()
