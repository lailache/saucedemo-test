import unittest

from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestSauceDemoPurchase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_purchase(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_information("Laila", "Che", "001")
        checkout_page.finish()

        self.assertTrue(checkout_page.is_order_complete())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
