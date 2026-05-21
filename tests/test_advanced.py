from playwright.sync_api import sync_playwright
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

# def networkMocking():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, args=["--ignore-certificate-errors"])
      
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://browserleaks.com/geo")
#         # context.clear_permissions()
#         page.wait_for_timeout(15000)



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


withCookies()





