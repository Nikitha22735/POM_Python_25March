from playwright.sync_api import expect, sync_playwright
def dimentionsM1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width":2301,"height":1200})
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(5000)


def mobileEmulations():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        print(p.devices)
        context = browser.new_context(**p.devices["iPhone XR"])
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(5000)

def networkMocking():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, args=["--ignore-certificate-errors"])
      
        context = browser.new_context(geolocation={"latitude": 37.269175, "longitude": -119.30661},
        permissions=["geolocation"])
        page = context.new_page()
        page.goto("https://browserleaks.com/geo")
        # context.clear_permissions()
        page.wait_for_timeout(15000)


# networkMocking()



def offlineMode():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # print(p.devices)
        context = browser.new_context()
        context.set_offline(True)
        page = context.new_page()
        
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(5000)




def withCookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # print(p.devices)
        context = browser.new_context(storage_state="auth.json")

        page = context.new_page()
        
        page.goto("https://www.amazon.in/")
        page.wait_for_timeout(5000)

# pip install pillow
from PIL import Image, ImageChops
def visualRegression():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # print(p.devices)
        context = browser.new_context()

        page = context.new_page()
        
        page.goto("https://testautomationpractice.blogspot.com/")
        # expect(page.locator("//button[text()='START']")).to_have_Screenshot("ss3.png")

        img1 = Image.open("ss3.png")
        img2 = Image.open("ss1.png")
        diff = ImageChops.difference(img1,img2)

        assert diff.getbbox() is None
        # page.screenshot(path="ss2.png", full_page=True)
        # page.locator("//button[text()='START']").screenshot(path='ss4.png')

        # page.wait_for_timeout(5000)















