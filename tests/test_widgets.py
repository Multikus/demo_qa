import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            page_accordian = AccordianPage(driver, 'https://demoqa.com/accordian')
            page_accordian.open()
            first_title, first_content = page_accordian.check_accordian('first')
            second_title, second_content = page_accordian.check_accordian('second')
            third_title, third_content = page_accordian.check_accordian('third')

            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "Сломан первый элемент аккордеона"
            assert second_title == 'Where does it come from?' and second_content > 0, "Сломан второй элемент аккордеона"
            assert third_title == 'Why do we use it?' and third_content > 0, "Сломан третий элемент аккордеона"

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            page_auto_complete = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            page_auto_complete.open()
            colors = page_auto_complete.fill_input_multiple()
            colors_result = page_auto_complete.check_color_in_multi()
            assert colors == colors_result, "Проблемы с множественным выбором значений"

        def test_remove_multi_autocomplete(self, driver):
            page_auto_complete = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            page_auto_complete.open()
            page_auto_complete.fill_input_multiple()
            count_value_before, count_value_after = page_auto_complete.remove_value_from_multi()
            assert count_value_before != count_value_after, "Проблема с удалением значения"

        def test_all_remove_multi_autocomplete(self, driver):
            page_auto_complete = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            page_auto_complete.open()
            page_auto_complete.fill_input_multiple()
            count_value_after = page_auto_complete.remove_all_value_from_multi()
            assert count_value_after == False, 'Проблема с удалением всех элементов инпута'

        def test_fill_single_autocomplete(self, driver):
            page_auto_complete = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            page_auto_complete.open()
            color = page_auto_complete.fill_input_single()
            color_result = page_auto_complete.check_color_in_single()
            assert color == color_result, 'Проблема в тесте инпута с одним значением'

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'Дата не изменилась'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'Дата не изменилась'

    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider_value()
            assert value_before != value_after, "Значения input range не изменилось"
            time.sleep(3)

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_pb_before, value_pb_after, button_change_text = progress_bar.change_progress_bar_value()
            assert value_pb_before != value_pb_after, "Значения progress bar не изменилось"
            assert button_change_text == 'Stop', "Текст на кнопке не менялся"

    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            assert what_button == 'What' and what_content != 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content != 0, 'the tab "origin" was not pressed or the text is missing'
            assert use_button == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'

    class TestToolTipsPage:

        def test_tool_tips_page(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, input_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'Ошибка с получением Tool tips'
            assert input_text == 'You hovered over the text field', 'Ошибка с получением Tool tips'
            assert contrary_text == 'You hovered over the Contrary', 'Ошибка с получением Tool tips'
            assert section_text == 'You hovered over the 1.10.32' , 'Ошибка с получением Tool tips'

    class TestMenuPage:

        def test_menu_item(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], 'Элементы меню не совпадают'
