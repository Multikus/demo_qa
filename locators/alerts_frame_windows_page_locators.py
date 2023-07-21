from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By. CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')

    TITLE_NEW = (By. CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By. CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_BUTTON_AFTER_5_SEC = (By. CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By. CSS_SELECTOR, 'button[id="confirmButton"]')
    PROMPT_BOX_ALERT_BUTTON = (By. CSS_SELECTOR, 'button[id="promtButton"]')

    # текст для проверки
    CONFIRM_RESULT = (By. CSS_SELECTOR, 'span[id="confirmResult"]')
    CONFIRM_PROMPT_RESULT = (By. CSS_SELECTOR, 'span[id="promptResult"]')


class FramePageLocators:
    FRAME_FIRST = (By. CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME_SECOND = (By. CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedPageLocators:
    FRAME_PARENT = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')

    CHILD_FRAME = (By. CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By. CSS_SELECTOR, 'p')


class ModalPageLocators:
    SMALL_MODAL_BUTTON = (By. CSS_SELECTOR, 'button[id="showSmallModal"]')
    CLOSE_SMALL_MODAL_BUTTON = (By. CSS_SELECTOR, 'button[id="closeSmallModal"]')
    TITLE_SMALL_MODAL = (By. CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    TEXT_SMALL_MODAL = (By. CSS_SELECTOR, 'div[class="modal-body"]')

    LARGE_MODAL_BUTTON = (By. CSS_SELECTOR, 'button[id="showLargeModal"]')
    CLOSE_LARGE_MODAL_BUTTON = (By. CSS_SELECTOR, 'button[id="closeLargeModal"]')
    TITLE_LARGE_MODAL = (By. CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    TEXT_LARGE_MODAL = (By. CSS_SELECTOR, 'div[class="modal-body"] p')


