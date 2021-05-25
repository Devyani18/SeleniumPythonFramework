import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_HomeForm(self, getFormData):

        homePage = HomePage(self.driver)
        log = self.commonLogger()
        log.debug("Entering first name : " + getFormData['firstname'])
        homePage.getNameTextbox().send_keys(getFormData['firstname'])
        log.debug("Entering email address : " + getFormData['email'])
        homePage.getEmailTextbox().send_keys(getFormData['email'])
        homePage.getIceCreamCheckbox().click()
        log.debug("Selecting gender : " + getFormData['gender'])
        self.selectTextFromDropdown(getFormData['gender'], homePage.getGenderDropdown())
        log.debug("Submitting the form")
        homePage.getSubmit().click()
        message = homePage.getMessage().text
        log.debug(message)
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=[HomePageData.getTestDataFromExcel("Person4"), HomePageData.getTestDataFromExcel("Person1")])
    def getFormData(self, request):
        return request.param
