from selenium.webdriver.common.by import By


# Локаторы для страницы demoqa.com/text-box
class TextBoxPageLocators:
    # Поля формы
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    FOOTER = (By.CSS_SELECTOR, "footer")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    # Создание формы
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


# Локаторы для страницы demoqa.com/checkbox
class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # popup поля
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
    # tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    # update person info
    UPDATE_BUTTON = (By. CSS_SELECTOR, 'span[title="Edit"]')
    # delete person
    CHECK_ROW_NO_FOUND = (By. CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    FOOTER = (By.CSS_SELECTOR, "footer")


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By. CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By. CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By. XPATH, '//button[text()="Click Me"]')
    # text
    SUCCESS_DOUBLE = (By. CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By. CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By. CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By. CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By. CSS_SELECTOR, 'a[id="bad-request"]')
    NOT_FOUND_LINK = (By. CSS_SELECTOR, 'a[id="invalid-url"]')


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By. CSS_SELECTOR, 'input[id="uploadFile"]')
    DOWNLOAD_FILE = (By. CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOADED_FILE = (By. CSS_SELECTOR, 'p[id="uploadedFilePath"]')


class DynamicPropertiesLocators:
    COLOR_CHANGE_BUTTON = (By. CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_BUTTON = (By. CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_BUTTON = (By. CSS_SELECTOR, 'button[id="enableAfter"]')
