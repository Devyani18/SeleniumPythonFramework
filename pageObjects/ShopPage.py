from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, ".card-title a")
    # self.driver.find_element_by_css_selector(".card-footer button")[i].click()
    footers = (By.CSS_SELECTOR, ".card-footer button")
    # self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
    checkout = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*ShopPage.cardTitles)

    def getFooters(self):
        return self.driver.find_elements(*ShopPage.footers)

    def getCheckout(self):
        self.driver.find_element(*ShopPage.checkout).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
