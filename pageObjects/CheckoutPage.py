from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    addedItemName = (By.XPATH, "//h4/a")
    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    finalCheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def getAddedItemName(self):
        return self.driver.find_element(*CheckoutPage.addedItemName)

    def getFinalCheckout(self):
        self.driver.find_element(*CheckoutPage.finalCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
