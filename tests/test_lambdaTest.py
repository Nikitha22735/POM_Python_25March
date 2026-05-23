import os
import json

from playwright.sync_api import expect, sync_playwright

capabilities = {
    'browserName': 'Chrome', #Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': '142',
    'LT:Options': {
      'platform': 'Windows 11',
      'build': 'Playwright Sample Build for march 25 batch',
      'name': 'Playwright Sample Test',
      'user': os.getenv("LT_USERNAME"),
      'accessKey':  os.getenv("LT_ACCESS_KEY"),
      'video': True
    }
  }

def test_lamdaTest():
    with sync_playwright() as p:
        browser = p.chromium.connect(f"wss://cdp.lambdatest.com/playwright?capabilities={json.dumps(capabilities)}")


        # print(p.devices)
        # context = browser.new_context()

        page = browser.new_page()
        
        page.goto("https://testautomationpractice.blogspot.com/")
        print(page.title())
        browser.close()