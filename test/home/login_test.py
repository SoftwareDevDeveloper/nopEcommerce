from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self):
        baseURL = "https://admin-demo.nopcommerce.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)

        self.lp = LoginPage(driver)

    @pytest.mark.regression
    @pytest.mark.run(order=2)
    def test_verifyLoginTitle(self):
        self.lp.login("admin@yourstore.com", "admin")
        result = self.lp.verifyLoginTitle()
        assert result == True

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.run(order=3)
    def test_validLogin(self):
        self.lp.login("admin@yourstore.com", "admin")
        result1 = self.lp.verifySuccessfulLogin()
        assert result1 == True

    @pytest.mark.regression
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("admin@yourstore.com", "administration")
        result2 = self.lp.verifyLoginUnsuccessful()
        assert result2 == True


































#
# @pytest.mark.run(order=2)
#     def test_validLogin(self):
#         self.lp.login("admin@yourstore.com", "admin")
#         result = self.lp.verifyLoginTitle()
#         self.ts.mark(result, "Test Passed")
#        # assert result == True
#         result1 = self.lp.verifySuccessfulLogin()
#         self.ts.markFinal("test_validLogin", result1, "Test verification passed")
#        # assert result1 == True
