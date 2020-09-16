from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities import logging as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def verifyPageTitle(self):
        return self.driver.title

    def screenShot(self, resultMessage):
        """
        Takes screenshots of the error page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f'The Screenshot was saved to directory: {destinationFile}')
        except:
            self.log.error("### Exception Occurred when taking screenshots")
            print_stack()

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'Element found with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Element not found with locator: {locator} and locatorType: {locatorType}')
        return element

    def getElementList(self, locator, locatorType="id"):
        # This Get list of elements
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info(f'Element list found with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Element list not found with locator: {locator} and locatorType: {locatorType}')
            return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'Clicked on the element with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Cannot click on the element with locator: {locator} and locatorType: {locatorType}')
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f'Sent data on the element with locator: {locator} and locatorType: {locatorType}')
        except:
            self.log.error(f'Cannot send data on the element with locator: {locator} and locatorType: {locatorType}')
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info(f'Element found with locator: {locator} and locatorType: {locatorType}')
                return True
            else:
                self.log.errort(f'Element not found with locator: {locator} and locatorType: {locatorType}')
                return False
        except:
            print("Element not found")
            return False

    def getText(self, locator="", locatorType="", element=None, info=""):
        print()

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info(f'Element found with locator: {locator} and locatorType: {byType}')
                return True
            else:
                self.log.error(f'Element not found with locator: {locator} and locatorType: {byType}')
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.log("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def scrollBrowser(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -800);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 800);")

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe
        Parameters:
        1. Required:
        None
        2. Optional:
        1. id    - id of the iframe
        2. name  - name of the iframe
        3. index - index of the iframe
        Returns: None
        Exception: None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content
        Parameters: None
        Returns: None
        Exception: None
        """
        self.driver.switch_to.default_content()









    # def random_generator(self, size=9, chars=string.ascii_lowercase + string.digits):
    #     return ''.join(random.choice(chars) for x in range(size)

   # pytest -s -v --html=base/report.html tests/home/login_test.py    ---- html report in the base package


   # pytest -s -v "Sanity"--html=base/report.html test/customer/search_customer_test.py


    # Push the code to Git and GitHub Repository

    # 1)Create an empty git repository(local repository)
    # git init

    # 2)Connect your local git(local rep) with github(global rep)
    # git remote add origin

    # 3)Checking the status of files(committed/not committed)
    # git status

    # 4)Add all the files to the staging area
    # git add -A   -----> Add all the files to staging/indexing area

    # 5)Commit the code into git repository(local rep)
    # git commit -m "comment"

    # 6)Push the code from git into the github repository)
    # git push -u origin master

    # 1) git pull
    # 2) git add -A  this command should follow after the new file has been added and updated
    # 3) git commit -m "comment"
#   # 4)git push -u origin master
