from src.helpers.helper_base import HelperBase


def schedule_buttons_iterator(driver, dictionary):
    helper = HelperBase(driver)

    for key, val in dictionary.items():
        schedule_button_is_present = helper.is_element_present_by_xpath(
            f'//android.widget.TextView[@text="{key}"]/../../android.widget.ImageView[3]')

        if schedule_button_is_present is not True:
            continue

        schedule_button = helper.find_by_xpath(f'//android.widget.TextView[@text="{key}"]')
        helper.click_by_element(schedule_button)
        helper.wait_activity(val)
        back_button = helper.find_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]')
        helper.click_by_element(back_button)

        helper.wait_activity('//android.widget.TextView[@text="Распорядок дня"]')
        helper.swipe_from_down_to_up()

def menu_buttons_iterator(driver, dictionary):
    helper = HelperBase(driver)

    for key, val in dictionary.items():
        menu_button_is_present = helper.is_element_present_by_xpath(f'//android.widget.CheckedTextView[@text="{key}"]')

        if menu_button_is_present is not True:
            continue

        menu_button = helper.find_by_xpath(f'//android.widget.CheckedTextView[@text="{key}"]')
        helper.click_by_element(menu_button)
        helper.wait_activity(val)
        element_in_screen = helper.find_by_xpath(val)

        if not (element_in_screen is None):
            helper.swipe_menu()
            helper.wait_activity('some.application.debug:id/tv_user_info')
            helper.swipe_menu_from_down_to_up()
