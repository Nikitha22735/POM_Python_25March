from playwright.sync_api import Page, expect

class loginPage:
    def __init__(self, page: Page):
        self.contnBtn = page.locator("//input[@type='submit']")
        self.emailtextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.pwtextbox = page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        self.emailErrorTxt =  page.locator("//div[contains(text(),'Invalid email address')]")


    def enterEmail(self,emailId):
        self.emailtextBox.fill(emailId)
    def clickOnContinueBtn(self):
         self.contnBtn.click()

    def enterPw(self,pw):
        self.pwtextbox.fill(pw)

    def clickOnSignBtn(self):
         self.signInBtn.click()

    def validateTheEmailError(self):
        expect(self.emailErrorTxt).to_be_visible()

