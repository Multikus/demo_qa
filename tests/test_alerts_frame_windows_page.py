import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedPage, ModalPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text = new_tab_page.check_opened_new_tab()
            assert text == 'This is a sample page', "Текст на новой странице не совпадает с ожиданием"

        def test_new_window(self, driver):
            new_win_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_win_page.open()
            text = new_win_page.check_opened_new_window()
            assert text == 'This is a sample page', "Текст на новой странице не совпадает с ожиданием"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            new_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            new_alert_page.open()
            text_alert = new_alert_page.check_see_alert()
            assert text_alert == 'You clicked a button'

        def test_check_alert_appear_5_sec(self, driver):
            new_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            new_alert_page.open()
            text_alert = new_alert_page.check_alert_appear_5_sec()
            assert text_alert == 'This alert appeared after 5 seconds', "Не получен текс предупрежедения через 5 секунд"

        def test_check_confirm_alert(self, driver):
            new_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            new_alert_page.open()
            text = new_alert_page.check_confirm_alert()
            assert text == 'You selected Ok', "Выбрана другая кнопка"

        def test_check_prompt_alert(self, driver):
            new_prompt_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            new_prompt_page.open()
            res_text, text = new_prompt_page.check_prompt_alert()
            assert res_text == f'You entered {text}'
            # как вариант для проверки
            assert text in res_text, "Текст в Prompt не совпадает с ожидаемым"

    class TestFramePage:

        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame_one = frame_page.check_frame('frame1')
            result_frame_two = frame_page.check_frame('frame2')
            assert result_frame_one == ['This is a sample page', '500px', '350px'], "Проблема во фрейме 1"
            assert result_frame_two == ['This is a sample page', '100px', '100px'], "Проблема во фрейме 2"

    class TestNestedFramePage:

        def test_nested_frames(self, driver):
            nested_page = NestedPage(driver, 'https://demoqa.com/nestedframes')
            nested_page.open()
            parent_text, child_text = nested_page.check_nested_frames()
            assert parent_text == 'Parent frame', "Ошибка в Parent frame"
            assert child_text == 'Child Iframe', "Ошибка в Child Iframe"

    class TestModalDialogs:

        def test_modal_dialogs(self, driver):
            modal_page = ModalPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_page.open()
            small, large = modal_page.check_modal_dialogs()
            assert small[1] < large[1], 'Текст совпадает по размеру или больше'
            assert small[0] == 'Small Modal', 'Ошибка в тесте маленького модального окна'
            assert large[0] == 'Large Modal', 'Ошибка в тесте большого модального окна'
