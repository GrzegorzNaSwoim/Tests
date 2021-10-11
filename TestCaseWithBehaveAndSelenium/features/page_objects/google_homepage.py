from selenium import webdriver
from selenium.webdriver.common.by import By


class FixtureBrowserSetup:
    def __init__(self):
        self._driver = webdriver.Chrome(executable_path=r'c:\ChromeDriver\chromedriver.exe')
        self._driver.implicitly_wait(5)

    def clean_up(self):
        self._driver.quit()


class GoogleSearch(FixtureBrowserSetup):
    SEARCH_INPUT = (By.XPATH, ".//input[@class='gLFyf gsfi']")
    SEARCH_BUTTON = (By.XPATH, ".//input[@class='gNO89b']")
    APROVE_BUTTON = (By.XPATH, ".//button[@id='L2AGLb']")
    LANGUAGE_SETTINGS = (By.LINK_TEXT, "polski")

    def __init__(self):
        super().__init__()
        self._page = self._driver.get("https://google.pl")

    def confirm_cookies(self):
        self._driver.find_element(*self.APROVE_BUTTON).click()

    def select_language(self):
        print('dupa')
        search = self._driver.find_elements(*self.SEARCH_BUTTON)
        if self._driver.find_elements(*self.SEARCH_BUTTON)[1].get_attribute('value') != 'Szukaj w Google':
            self._driver.find_element(*self.LANGUAGE_SETTINGS).click()

    def input_search_text(self, text: str):
        search = self._driver.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(text)

    def click_search_button(self):
        button = self._driver.find_elements(*self.SEARCH_BUTTON)
        button[1].click()


if __name__ == '__main__':
    google = GoogleSearch()
    google.confirm_cookies()
    google.select_language()
