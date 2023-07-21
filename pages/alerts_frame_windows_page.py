import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramePageLocators, NestedPageLocators, ModalPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        check_text = self.element_is_present(self.locators.TITLE_NEW).text
        return check_text

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        check_text = self.element_is_present(self.locators.TITLE_NEW).text
        return check_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_win = self.driver.switch_to.alert.text
        return alert_win

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_BUTTON_AFTER_5_SEC).click()
        time.sleep(5.1)
        alert_win = self.driver.switch_to.alert.text
        return alert_win

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_win = self.driver.switch_to.alert
        alert_win.accept()
        text_res = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_res

    def check_prompt_alert(self):
        text = f'You entered {random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_win = self.driver.switch_to.alert
        alert_win.send_keys(text)
        alert_win.accept()
        text_res = self.element_is_present(self.locators.CONFIRM_PROMPT_RESULT).text
        return text_res, text


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME_FIRST)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME_SECOND)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedPage(BasePage):
    locators = NestedPageLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.FRAME_PARENT)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalPage(BasePage):
    locators = ModalPageLocators()

    def check_modal_dialogs(self,):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.TEXT_SMALL_MODAL).text
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.TEXT_LARGE_MODAL).text
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL_BUTTON).click()
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]
