import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def commonLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('D:\Study\Automation\SeleniumPython\seleniumPython\FrameworkPythonSelenium\TestScripts\Logs\\testlog.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def getLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectTextFromDropdown(self, gender, locator):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(gender)
