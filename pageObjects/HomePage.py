from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    nameTextbox = (By.CSS_SELECTOR, "input[name='name']")
    emailTextbox = (By.NAME, "email")
    iceCreamCheckbox = (By.ID, "exampleCheck1")
    genderDropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.CLASS_NAME, "btn-success")
    message = (By.CLASS_NAME, "alert-success")

    def goToShop(self):
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage

    def getNameTextbox(self):
        return self.driver.find_element(*HomePage.nameTextbox)

    def getEmailTextbox(self):
        return self.driver.find_element(*HomePage.emailTextbox)

    def getIceCreamCheckbox(self):
        return self.driver.find_element(*HomePage.iceCreamCheckbox)

    def getGenderDropdown(self):
        return self.driver.find_element(*HomePage.genderDropdown)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
