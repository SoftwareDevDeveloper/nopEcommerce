from pages.home.login_page import LoginPage
from pages.customer.search_customer import SearchACustomer
from selenium import webdriver
import unittest
import pytest

class SearchCustomer(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        baseURL = "https://admin-demo.nopcommerce.com/Admin/Customer/List"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)

        self.lp = LoginPage(driver)
        self.sc = SearchACustomer(driver)


    @pytest.mark.sanity
    @pytest.mark.run(order=2)
    def test_verifySearchPageTitle(self):
        self.lp.login("admin@yourstore.com", "admin")
        result = self.sc.searchPageOpened()
        assert result == True

    @pytest.mark.regression
    @pytest.mark.run(order=3)
    def test_verifyCustomerNotFound(self):
        result = self.sc.unSuccessfulCustomerSearch()
        assert result == True

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.run(order=1)
    def test_searchByEmail(self):
        self.lp.login("admin@yourstore.com", "admin")
        result = self.sc.enterEmail("villanueva_00@yopmail.com")
        assert result == True




