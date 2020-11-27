from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class HelperBase:

    def __init__(self, driver):
        self.driver = driver

    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_by_class(self, className):
        return self.driver.find_element_by_class_name(className)

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def click_by_element(self, element):
        element.click()

    def wait_activity(self, element, timeout=1, interval=1):
        self.driver.wait_activity(element, timeout, interval)

    def clear_field(self, element):
        element.clear()

    def set_value(self, element, value):
        self.driver.set_value(element, value)

    def get_text_by_id(self, id):
        return self.driver.find_element_by_id(id).text

    def get_text_by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name).text

    def get_text_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text

    def check_text_by_id(self, element, text_for_check, time_to_wait_present, interval):
        self.wait_activity(element, time_to_wait_present, interval)
        text = self.get_text_by_id(element)
        assert text == text_for_check

    def check_text_by_xpath(self, element, text_for_check, time_to_wait_present, interval):
        self.wait_activity(element, time_to_wait_present, interval)
        text = self.get_text_by_xpath(element)
        assert text == text_for_check

    def scroll_from_to(self, element1, element2):
        actions = TouchAction(self.driver)
        actions.press(element1).move_to(element2).release().perform()

    def swipe_menu(self):
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.01
        end_x = size['width'] * 0.3
        start_y = size['height'] / 2
        self.driver.swipe(start_x, start_y, end_x, start_y, 500)

    def swipe_from_down_to_up(self):
        size = self.driver.get_window_size()
        start_y = size['height'] * 0.5
        end_y = size['height'] * 0.4
        start_x = size['width'] / 2
        self.driver.swipe(start_x, start_y, start_x, end_y, 500)

    def swipe_menu_from_down_to_up(self):
        size = self.driver.get_window_size()
        start_y = size['height'] * 0.5
        end_y = size['height'] * 0.4
        start_x = size['width'] / 4
        self.driver.swipe(start_x, start_y, start_x, end_y, 500)

    def is_enabled(self, element):
        return element.is_enabled()

    def is_element_present_by_xpath(self, element):
        try:
            self.find_by_xpath(element)
            return True
        except NoSuchElementException:
            return False
