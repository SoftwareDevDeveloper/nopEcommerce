from pages.home.login_page import LoginPage
from pages.customer.add_customer_page import AddNewCustomerPage
from base.selenium_driver import SeleniumDriver
from selenium import webdriver
import unittest
import pytest
import random
import string


class AddCustomer(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        baseURL = "https://admin-demo.nopcommerce.com/Admin/Customer/Create"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(baseURL)

        self.lp = LoginPage(self.driver)
        self.ad = AddNewCustomerPage(self.driver)
        self.sd = SeleniumDriver(self.driver)


    @pytest.mark.sanity
    @pytest.mark.run(order=1)
    def test_verifyNewCustomerPageTitle(self):
        self.lp.login("admin@yourstore.com", "admin")
        result = self.ad.verifyCustomerAddedPageIsOpen()
        assert result == True

    @pytest.mark.regression
    @pytest.mark.run(order=2)
    def test_addNewCustomer(self):
        self.lp.login("admin@yourstore.com", "admin")
        self.ad.openAddCustomerPage()
        self.ad.enterCustomerPrimaryDetails(email=self.random_generator() + "@gmail.com", password="test123", firstname="Jamie", lastname="Josh")
        self.ad.setGender("Male")
        self.ad.enterDateOfBirth("7/02/2000")
        self.ad.enterCompanyName("Infrastructure Group Limited")
        self.ad.clickTaxExempt()
        self.ad.setCustomerRoles("Vendor")
        self.ad.setManagerOfVendor("Vendor 1")
        self.ad.selectActiveCheckBox()
        self.ad.enterAdminComment("We are creating a new customer page")
        self.ad.clickSaveButton()

        newCustomerAdded = self.sd.getText(locator="body", locatorType="tag_name")
        print(newCustomerAdded)

        if "customer has been added successfully." in newCustomerAdded:
            assert True == True
        else:
            result = self.driver.save_screenshot("./screenshots/" + "test_AddNewCustomer_scr.png")
            assert result == False

    def random_generator(self, size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
