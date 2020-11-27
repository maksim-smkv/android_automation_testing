from src.helpers.helper_base import HelperBase
from src.helpers.init_config import InitConfig


def open_and_fill_login_pass_fields(driver):
    helper = HelperBase(driver)

    login_field = helper.find_by_id('some.application.debug:id/et_login')
    helper.click_by_element(login_field)
    helper.set_value(login_field, InitConfig.userName)

    pass_field = helper.find_by_id('some.application.debug:id/et_password')
    helper.click_by_element(pass_field)
    helper.set_value(pass_field, InitConfig.userPass)

    continue_btn = helper.find_by_id('some.application.debug:id/btn_login')
    helper.click_by_element(continue_btn)


def open_and_fill_phone_pass_fields(driver):
    helper = HelperBase(driver)

    login_by_phone_btn = helper.find_by_id('some.application.debug:id/tv_login_by_phone')
    helper.click_by_element(login_by_phone_btn)

    helper.wait_activity('some.application.debug:id/et_login', 2, 1)

    phone_field = helper.find_by_id('some.application.debug:id/et_login')
    helper.click_by_element(phone_field)
    helper.set_value(phone_field, InitConfig.userPhone)

    sms_pass_field = helper.find_by_id('some.application.debug:id/et_password')
    helper.click_by_element(sms_pass_field)
    helper.set_value(sms_pass_field, InitConfig.userSmsPass)

    show_pass_btn = helper.find_by_id('some.application.debug:id/text_input_end_icon')
    helper.click_by_element(show_pass_btn)

    continue_btn = helper.find_by_id('some.application.debug:id/btn_login')
    helper.click_by_element(continue_btn)


def fill_office_shk_field(driver):
    helper = HelperBase(driver)

    office_shk_field = helper.find_by_id('some.application.debug:id/et_office_shk')
    helper.click_by_element(office_shk_field)
    helper.set_value(office_shk_field, InitConfig.officeShK)

    continue_btn = helper.find_by_id('some.application.debug:id/btn_continue')
    helper.click_by_element(continue_btn)


def assert_schedule_page_header(driver):
    helper = HelperBase(driver)

    helper.wait_activity('android.widget.TextView', 3, 1)
    header_text = helper.get_text_by_class('android.widget.TextView')
    assert header_text == "Распорядок дня"


def login_pass_form_iterator(driver, dictionary):
    helper = HelperBase(driver)

    helper.wait_activity('some.application.debug:id/et_login')
    login_field = helper.find_by_id('some.application.debug:id/et_login')
    pass_field = helper.find_by_id('some.application.debug:id/et_password')

    for key, val in dictionary.items():
        helper.wait_activity(login_field)
        helper.click_by_element(login_field)
        helper.clear_field(login_field)
        helper.set_value(login_field, key)

        helper.click_by_element(pass_field)
        helper.clear_field(pass_field)
        helper.set_value(pass_field, val)

        show_pass_btn = helper.find_by_id('some.application.debug:id/text_input_end_icon')
        helper.click_by_element(show_pass_btn)

        continue_btn = helper.find_by_id('some.application.debug:id/btn_login')

        if key is None or val is None:
            continue_btn_enabled_state = helper.is_enabled(continue_btn)
            if continue_btn_enabled_state is False:
                continue

        helper.click_by_element(continue_btn)

        helper.wait_activity('some.application.debug:id/title')
        popup_header_text = helper.get_text_by_id('some.application.debug:id/title')
        assert popup_header_text == "Неверный логин или пароль"

        popup_ok_btn = helper.find_by_id('android:id/button1')
        helper.click_by_element(popup_ok_btn)


def phone_pass_form_iterator(driver, dictionary):
    helper = HelperBase(driver)

    login_by_phone_btn = helper.find_by_id('some.application.debug:id/tv_login_by_phone')
    helper.click_by_element(login_by_phone_btn)

    helper.wait_activity('some.application.debug:id/et_login')

    phone_field = helper.find_by_id('some.application.debug:id/et_login')
    sms_pass_field = helper.find_by_id('some.application.debug:id/et_password')

    for key, val in dictionary.items():
        helper.wait_activity(phone_field)
        helper.click_by_element(phone_field)
        helper.clear_field(phone_field)
        helper.set_value(phone_field, key)

        helper.click_by_element(sms_pass_field)
        helper.clear_field(sms_pass_field)
        helper.set_value(sms_pass_field, val)

        show_pass_btn = helper.find_by_id('some.application.debug:id/text_input_end_icon')
        helper.click_by_element(show_pass_btn)

        continue_btn = helper.find_by_id('some.application.debug:id/btn_login')

        if key is None or val is None or len(key) < 10 or len(val) < 6 or len(val) > 6:
            continue_btn_enabled_state = helper.is_enabled(continue_btn)
            if continue_btn_enabled_state is False:
                continue

        helper.click_by_element(continue_btn)

        helper.wait_activity('some.application.debug:id/title')
        popup_header_text = helper.get_text_by_id('some.application.debug:id/title')
        assert popup_header_text == "Неверный логин или пароль"

        popup_ok_btn = helper.find_by_id('android:id/button1')
        helper.click_by_element(popup_ok_btn)


def office_shk_form_iterator(driver, office_shk_list):
    helper = HelperBase(driver)

    office_shk_field = helper.find_by_id('some.application.debug:id/et_office_shk')

    for value in office_shk_list:
        helper.wait_activity(office_shk_field)
        helper.click_by_element(office_shk_field)
        helper.clear_field(office_shk_field)
        helper.set_value(office_shk_field, value)

        continue_btn = helper.find_by_id('some.application.debug:id/btn_continue')

        if value is None or len(value) < 14 or len(value) > 14:
            continue_btn_enabled_state = helper.is_enabled(continue_btn)
            if continue_btn_enabled_state is False:
                continue

        helper.click_by_element(continue_btn)

        helper.wait_activity('some.application.debug:id/title')
        popup_header_text = helper.get_text_by_id('some.application.debug:id/title')
        assert popup_header_text == "Ошибка"

        popup_ok_btn = helper.find_by_id('android:id/button1')
        helper.click_by_element(popup_ok_btn)
