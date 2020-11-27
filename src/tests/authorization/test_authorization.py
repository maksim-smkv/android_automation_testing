from src.helpers.helper_base import HelperBase
import src.helpers.authorization_helper as auth_helper
import pytest


@pytest.mark.usefixtures("init_driver")
class TestAuthorization:
    driver = None

    @pytest.mark.usefixtures("open_close_app_per_test")
    def test_authorization_via_login(self):
        # ввести валидный логин, пароль и перейти на экран с вводом ШК офиса
        auth_helper.open_and_fill_login_pass_fields(self.driver)

        # ввести ШК офиса и перейти на экран "Распорядок дня"
        auth_helper.fill_office_shk_field(self.driver)

        # проверить наличие текста "Распорядок дня" на главном экране
        auth_helper.assert_schedule_page_header(self.driver)

    @pytest.mark.usefixtures("open_close_app_per_test")
    def test_authorization_via_phone(self):
        # ввести валидный номер телефона, пароль и перейти на экран с вводом ШК офиса
        auth_helper.open_and_fill_phone_pass_fields(self.driver)

        # ввести ШК офиса и перейти на экран "Распорядок дня"
        auth_helper.fill_office_shk_field(self.driver)

        # проверить наличие текста "Распорядок дня" на главном экране
        auth_helper.assert_schedule_page_header(self.driver)

    @pytest.mark.usefixtures("open_close_app_per_test")
    def test_shk_office_screen(self):
        helper = HelperBase(self.driver)

        # перейти на экран с вводом ШК офиса
        auth_helper.open_and_fill_login_pass_fields(self.driver)

        # открыть/закрыть сканер
        scanner_btn = helper.find_by_id('some.application.debug:id/tv_scan')
        helper.click_by_element(scanner_btn)

        close_scanner_btn = helper.find_by_id('some.application.debug:id/iv_close')
        helper.click_by_element(close_scanner_btn)

        # провилидировать поле "ШК офиса"
        office_shk_list = [None, 'OFFC1', 'OFFC1234567890', 'OFFC12345678900', 'офис1234567890', '@#%&++-&%$#@@$']

        auth_helper.office_shk_form_iterator(self.driver, office_shk_list)

    @pytest.mark.usefixtures("open_close_app_per_test")
    def test_negative_authorization_via_login(self):
        # провалидировать форму
        login_pass_dictionary = {None: '12345',
                                 '12345': None,
                                 '123456789': '123456789',
                                 '12345678': 'abcdefg',
                                 'abcd': '!@#$',
                                 'abcde': '123456789',
                                 'abcdef': None,
                                 'abcdefg': 'абвгде',
                                 'абвг': 'абвгде',
                                 'абвгд': '!@#$$%',
                                 '!@#$$%': 'абвгде',
                                 '!@#$$%^': None}

        auth_helper.login_pass_form_iterator(self.driver, login_pass_dictionary)

    @pytest.mark.usefixtures("open_close_app_per_test")
    def test_negative_authorization_via_phone(self):
        # провалидировать форму
        phone_pass_dictionary = {None: '123456',
                                 '1234567890': None,
                                 '9876543210': '123456',
                                 '9876543211': '123456789',
                                 '9876543212': '12345',
                                 '000000000': '123456'}

        auth_helper.phone_pass_form_iterator(self.driver, phone_pass_dictionary)
