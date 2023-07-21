import random

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage
import time


@allure.suite('Elements')
class TestElements:

    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check Text Box - проверяем чекбоксы')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_full_name, "Полное имя не совпадает"
            assert email == output_email, "Разная электронная почта"
            assert current_address == output_current_address, "Не совпадает адрес прописки"
            assert permanent_address == output_permanent_address, "Не совпадает фактический адрес"
            time.sleep(4)

    @allure.feature('CheckBox')
    class TestCheckBox:

        @allure.title('Check check Box - проверяем чекбоксы 2')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_checkboxes = check_box_page.get_output_result()
            assert input_checkboxes == output_checkboxes, "Какие-то чекбоксы не совпадают с ответом"

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title('Check Radio Button - проверяем радиокнопки 3')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "Have not been selected RADIOBUTTON YES"
            assert output_impressive == 'Impressive', "Have not been selected RADIOBUTTON IMPRESSIVE"
            assert output_no == 'No', "Have not been selected RADIOBUTTON NO"

    @allure.feature('WebTable')
    class TestWebTable:
        @allure.title('Check Web Table - проверяем таблицы 4')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            input_person = web_table_page.add_new_person()
            output_data_person = web_table_page.check_new_added_person()
            assert input_person in output_data_person, "New added person missing from the table"

        @allure.title('Check table search person - проверяем поиск информации в таблице 5')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "Элемент не найден в таблице"

        @allure.title('Check update person info - проверяем обновление информации о сотруднике')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "Изменение данных по человеку не проходит"

        @allure.title('Check table delete person - проверяем удаление  информации из таблицы')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            delete_info = web_table_page.check_delete()
            assert delete_info == 'No rows found', "Удаление строки данных не проходит"

        @allure.title('Check table change count row - проверяем изменение  кол-ва строк в таблице')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "Добавление строк работает не работает"

    class TestButtonsPage:

        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_button('double')
            click = buttons_page.click_on_different_button('click')
            right = buttons_page.click_on_different_button('right')
            assert double == "You have done a double click", "Тест на двойной клик не проходит"
            assert right == "You have done a right click", "Тест ПКМ не проходит"
            assert click == "You have done a dynamic click", "Тест клика провален"

    class TestLinksPage:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "Ссылки не совпадают"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert status == 400, "Тест на ошибку 400"

        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status = links_page.check_broken_link('https://demoqa.com/invalid-url')
            assert status == 404, "Тест на ошибку 404"

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            upload_file_name, text_upload_file_path = upload_page.upload_file()
            assert upload_file_name in text_upload_file_path, 'Выгрузка файла не удалась'

        def test_download_file(self, driver):
            links_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            links_page.open()
            answer_check_file = links_page.download_file()
            assert answer_check_file is True, "Файл не найден. Проблема с загрузкой файла"

    class TestDynamicProperties:

        def test_dynamic_properties(self, driver):
            properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            properties_page.open()
            color_a = properties_page.check_changed_of_color()
            assert color_a != 'rgba(255, 255, 255, 1)'

        def test_appears_of_button(self, driver):
            appears_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            appears_properties_page.open()
            appear = appears_properties_page.check_appears_of_button()
            assert appear is True, "Элемент отсутствует"

        def test_enable_of_button(self, driver):
            enable_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            enable_properties_page.open()
            enable_btn = enable_properties_page.check_enable_button()
            assert enable_btn is True, 'Кликнуть не получилось'
