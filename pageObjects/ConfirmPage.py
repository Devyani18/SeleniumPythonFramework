from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("country").send_keys("ind")
    countryTextbox = (By.ID, "country")
    # self.driver.find_element_by_link_text("India").click()
    india = (By.LINK_TEXT, "India")
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element_by_css_selector("input[type='submit']").click()
    purchaseBtn = (By.CSS_SELECTOR, "input[type='submit']")
    # self.driver.find_element_by_css_selector("div[class*='alert-success']")
    message = (By.CSS_SELECTOR, "div[class*='alert-success']")
    closeMsg = (By.CSS_SELECTOR, "a[class='close']")

    def getCountryTextbox(self):
        return self.driver.find_element(*ConfirmPage.countryTextbox)

    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.india)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getMessage(self):
        return self.driver.find_element(*ConfirmPage.message)

    def getCloseMsg(self):
        return self.driver.find_element(*ConfirmPage.closeMsg)
