from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Item in basket is presented, but should not be"

    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text == "Your basket is empty. Continue shopping", "Empty message is not presented"