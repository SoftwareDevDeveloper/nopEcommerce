from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators
    emailField = "Email"
    passwordField = "Password"
    checkBox = "//input[@type='checkbox']"
    loginButton = "//input[@class='button-1 login-button']"

    def clearFields(self):
        self.getElement(locator=self.emailField).clear()
        self.getElement(locator=self.passwordField).clear()

    def enterUsername(self, email):
        self.sendKeys(email, locator=self.emailField, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, locator=self.passwordField, locatorType="id")

    def clickCheckBox(self):
        self.elementClick(locator=self.checkBox, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(locator=self.loginButton, locatorType="xpath")

    def login(self, email, password):
        self.clearFields()
        self.enterUsername(email)
        self.enterPassword(password)
        self.clickCheckBox()
        self.clickLoginButton()

    def verifySuccessfulLogin(self):
        successfulLogin = self.isElementPresent(locator="Catalog", locatorType="link")
        return successfulLogin

    def verifyLoginUnsuccessful(self):
        loginFailed = self.isElementDisplayed(locator="//div[@class]contains(text(),'Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect')]", locatorType="xpath")
        return loginFailed

    def verifyLoginTitle(self):
        if "Dashboard" in self.verifyPageTitle():
            return True
        else:
            return False

    # def verifyLoginTitle(self):
    #     return self.verifyPageTitle("Dashboard")





































    # 3
    # def enterUsername(self, username):
    #     self.getEmailField().send_keys(username)
    #
    # def enterPassword(self, password):
    #     self.getPasswordField().send_keys(password)
    #
    # def clickCheckBox(self):
    #     self.getCheckBox().click()
    #
    # def clickLoginButton(self):
    #     self.getLoginButton().click()


    # 2
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self.emailField)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self.passwordField)
    #
    # def getCheckBox(self):
    #     return self.driver.find_element(By.XPATH, self.checkBox)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self.loginButton)
    #


    # 1
    # def login(self, username, password):
    #     emailField = self.driver.find_element(By.ID, "Email")
    #     emailField.clear()
    #     emailField.send_keys(username)
    #
    #     passwordField = self.driver.find_element_by_id("Password")
    #     passwordField.clear()
    #     passwordField.send_keys(password)
    #
    #     checkBox = self.driver.find_element_by_xpath("//input[@type='checkbox']")
    #     checkBox.click()
    #
    #     loginButton = self.driver.find_element_by_xpath("//input[@class='button-1 login-button']")
    #     loginButton.click()

