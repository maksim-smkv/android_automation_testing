from src.helpers.helper_base import HelperBase
from src.helpers.init_config import InitConfig
from datetime import date
import src.helpers.schedule_helper as schedule_helper
import src.helpers.authorization_helper as auth_helper
import pytest


@pytest.mark.usefixtures("init_driver")
class TestSchedule:
    driver = None

    @pytest.mark.usefixtures("open_close_app_per_test")
    def test_screen_schedule(self):
        helper = HelperBase(self.driver)

        # авторизация
        auth_helper.open_and_fill_login_pass_fields(self.driver)
        auth_helper.fill_office_shk_field(self.driver)

        # проверить каждую кнопку на экране "Распорядок дня"
        schedule_buttons_name_and_header_name = {'Прийти на работу': '//android.widget.Button[@text="Вход"]',
                                                 'Прием коробок': '//android.widget.LinearLayout[@content-desc="Прием"]',
                                                 'Прием вещей на волнорез': '//android.widget.LinearLayout[@content-desc="Сканирование"]',
                                                 'Сканировать возвраты/отказы': '//android.widget.LinearLayout[@content-desc="Возврат на склад"]',
                                                 'Переместить вещи': '//android.widget.LinearLayout[@content-desc="Перемещение"]',
                                                 'Уйти с работы': '//android.widget.LinearLayout[@content-desc="Выход"]'}

        schedule_helper.schedule_buttons_iterator(self.driver, schedule_buttons_name_and_header_name)

        # проверить каждую кнопку в меню
        burger_menu_button = helper.find_by_xpath(
            '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
        helper.click_by_element(burger_menu_button)
        helper.wait_activity('some.application.debug:id/tv_user_info')
        user_name = helper.get_text_by_id('some.application.debug:id/tv_user_info')
        pvz_name = helper.get_text_by_id('some.application.debug:id/tv_office')
        assert user_name == InitConfig.fullUserName
        assert pvz_name == InitConfig.pvzName

        menu_buttons_name_and_header_name = {'Возврат товара': '//android.widget.EditText[@text="Поиск клиента"]',
                                             'Инвентаризация': '//android.widget.TextView[@text="Место хранения не выбрано"]',
                                             'Вещи в офисе': '//android.widget.EditText[@text="Поиск вещей"]',
                                             'Коробки в офисе': '//android.widget.TextView[@text="Список"]',
                                             'Движение вещей': f'//android.widget.TextView[@text="{date.today().strftime("%d.%m.%Y")}"]',
                                             'Отгрузки': '//android.widget.TextView[@text="Коробка не отсканирована"]',
                                             'Инструкции': '//android.widget.TextView[@text="Инструкции"]',
                                             'Уведомления': '//android.widget.CompoundButton[@text="Все"]',
                                             'Настройки': '//android.widget.TextView[@text="Режим сканирования"]',
                                             'Выход': '//android.widget.TextView[@text="Выход из учетной записи"]'}

        schedule_helper.menu_buttons_iterator(self.driver, menu_buttons_name_and_header_name)
