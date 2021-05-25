from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestShop_e2e(BaseClass):

    def test_shope2e(self):

        homePage = HomePage(self.driver)
        log = self.commonLogger()
        log.info("Going to Shop page..")
        shopPage = homePage.goToShop()
        log.info("Getting card titles..")
        cards = shopPage.getCardTitles()
        log.info("Adding Blackberry to cart..")
        i = -1
        for card in cards:
            i = i + 1
            cardTitle = card.text
            print(cardTitle)
            if cardTitle == "Blackberry":
                shopPage.getFooters()[i].click()

        checkoutPage = shopPage.getCheckout()
        assert checkoutPage.getAddedItemName().text == "Blackberry"
        log.info("Checking Out..")
        confirmPage = checkoutPage.getFinalCheckout()
        confirmPage.getCountryTextbox().send_keys("ind")
        self.getLinkPresence("India")
        log.info("Selecting Country - India")
        confirmPage.getIndia().click()
        confirmPage.getCheckBox().click()
        log.info("Purchase!")
        confirmPage.getPurchaseBtn().click()
        successMsg = confirmPage.getMessage().text
        log.info(successMsg)
        assert "Success" in successMsg
        # self.driver.get_screenshot_as_file("screenshot.png")
        confirmPage.getCloseMsg().click()
