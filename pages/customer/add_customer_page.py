from base.selenium_driver import SeleniumDriver
import time


class AddNewCustomerPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators
    customerDropDownMenu = "//a[@href='#']//span[contains(text(),'Customers')]"
    customerSubMenu = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    addNewButton = "//a[@class='btn bg-blue']"
    emailField = "Email"
    passwordField = "Password"
    firstNameField = "FirstName"
    lastNameField = "LastName"
    maleGenderRadioBox = "Gender_Male"
    femaleGenderRadioBox = "Gender_Female"
    dateOfBirthField = "DateOfBirth"
    companyNameField = "Company"
    isTaxExemptRadio = "IsTaxExempt"
    customerRolesField = "SelectedCustomerRoleIds"
    itemAdministrator = "//li[contains(text(),'Administrators')]"
    itemRegistered = "//li[contains(text(),'Registered')]"
    itemVendor = "//li[contains(text(),'Vendors')]"
    itemGuest = "//li[contains(text(),'Guests')]"
    managerOfVendorField = "VendorId"
    activeCheckBox = "Active"
    adminCommentField = "AdminComment"
    saveButton = "save"  # name

    def clickCustomerDropDown(self):
        self.elementClick(locator=self.customerDropDownMenu, locatorType="xpath")

    def clickCustomer(self):
        self.elementClick(locator=self.customerSubMenu, locatorType="xpath")

    def clickAddNewButton(self):
        self.elementClick(self.addNewButton, locatorType="xpath")

    def openAddCustomerPage(self):   # This wrap the above 3 methods together
        self.clickCustomerDropDown()
        self.clickCustomer()
        self.clickAddNewButton()

    def enterEmail(self, email):
        self.sendKeys(email, locator=self.emailField)

    def enterPassword(self, password):
        self.sendKeys(password,locator=self.passwordField)

    def enterFirstName(self, firstname):
        self.sendKeys(firstname, locator=self.firstNameField)

    def enterLastName(self, lastname):
        self.sendKeys(lastname, locator=self.lastNameField)

    def enterCustomerPrimaryDetails(self, email, password, firstname, lastname):  # This wrap the above 4 methods together
        self.enterEmail(email)
        self.enterPassword(password)
        self.enterFirstName(firstname)
        self.enterLastName(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.elementClick(locator=self.maleGenderRadioBox)
        elif gender == "Female":
            self.elementClick(locator=self.femaleGenderRadioBox)
        else:
            self.elementClick(locator=self.maleGenderRadioBox)

    def enterDateOfBirth(self, dob):
        self.sendKeys(dob, locator=self.dateOfBirthField)

    def enterCompanyName(self, name):
        self.sendKeys(name, locator=self.companyNameField)

    def clickTaxExempt(self):
        self.elementClick(locator=self.isTaxExemptRadio)

    def selectActiveCheckBox(self):
        self.elementClick(locator=self.activeCheckBox)

    def enterAdminComment(self, comment):
        self.sendKeys(comment, locator=self.adminCommentField)

    def clickSaveButton(self):
        self.elementClick(locator=self.saveButton, locatorType="name")

    def clickLogOut(self):
        self.elementClick(locator="//a[@href][contains(text(),'Logout')]", locatorType="xpath")

    def verifyCustomerAddedPageIsOpen(self):
        elementCheck = self.isElementPresent(locator="back to customer list", locatorType="link")
        return elementCheck


    def setCustomerRoles(self, role):
        self.sendKeys(role, locator=self.customerRolesField)
        time.sleep(3)
        if role == "Registered":
            myList = self.getElement(locator=self.itemAdministrator, locatorType="xpath")
            return myList

        elif role == "Guests":
           # Here, the selection can only be guest or registered, not both
            time.sleep(3)
            self.elementClick("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")
            myList1 = self.getElement(locator=self.itemGuest, locatorType="xpath")
            return myList1

        elif role == "Vendor":
            myList2 = self.getElement(locator=self.itemVendor, locatorType="xpath")
            return myList2

        elif role == "Administrator":
            myList3 = self.getElement(locator=self.itemAdministrator, locatorType="xpath")
            return myList3
        else:
            defaultSelection = self.getElement(locator=self.itemGuest, locatorType="xpath")
            self.driver.execute_script("arguments[0].click;", defaultSelection)

    def setManagerOfVendor(self, value):
        drp = (self.getElement(locator=self.managerOfVendorField))
        drp.select_by_visible_text(value)

