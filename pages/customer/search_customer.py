from base.selenium_driver import SeleniumDriver
import time


class SearchACustomer(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver

    # locators
    emailField = "//input[@id='SearchEmail']"
    firstNameField = "SearchFirstName"
    searchButton = "//button[@id='search-customers']"

    def clearFields(self):
        field = self.getElement(locator=self.emailField, locatorType="xpath")
        field.clear()
        fields = self.getElement(locator=self.firstNameField)
        fields.clear()

    def enterEmail(self, email):
        self.sendKeys(email, locator=self.emailField,locatorType="xpath")

    def enterFirstName(self, firstname):
        self.sendKeys(firstname, locator=self.firstNameField)

    def clickSearchButton(self):
        self.elementClick(locator=self.searchButton)

    def unSuccessfulCustomerSearch(self):
        errorMessage = self.isElementPresent(locator="//td[@class='dataTables_empty'][contains(text(),'No data available in table')]", locatorType="xpath")
        return errorMessage

    def searchPageOpened(self):
        resultElement = self.isElementPresent(locator="//div[@class='search-text'][contains(text(),'Search')]", locatorType="xpath")
        return resultElement

    def searchCustomerByEmail(self, email):
        self.sendKeys(email, locator=self.emailField, locatorType="xpath")
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@id='search-customers']").click()



























    # def verifySearchPageTitle(self):
    #     if "Customer/List" in self.verifySearchPageTitle():
    #         return True
    #



    # wholeTableResult = "//table[@id='customers-grid']"
    # tableRow = "//table[@role='grid']"
    # allTableRows = "//table[@id='customers-grid']//tbody/tr"
    # allTableColumns = "//table[@id='customers-grid']//tbody/tr/td"

    # def clickCustomerDropDown(self):
    #     self.elementClick(locator=self.customerDropDownMenu, locatorType="xpath")
    #
    # def clickCustomer(self):
    #     self.elementClick(locator=self.customerSubMenu, locatorType="xpath")

    # def getNumberOfRows(self):
    #     return len(self.getElement(locator=self.allTableRows, locatorType="xpath"))
    #
    # def getNumberOfColumns(self):
    #     return len(self.getElement(locator=self.allTableColumns, locatorType="xpath"))
