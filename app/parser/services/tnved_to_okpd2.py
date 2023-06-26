import time

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Okpd2Data:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name


def convert_tnved_to_okpd2(tnved_code: str, driver) -> Okpd2Data:

    try:
        # Переходим на сайт
        driver.get('https://xn--b1ae8e.xn--p1ai/konverner-tnved-okpd/')
        # Находим поле ввода и вводим значение "НКУ"
        search_input = driver.find_element(By.ID, 'user-input')
        search_input.send_keys(f'{tnved_code}')
        # Находим кнопку поиска и нажимаем на неё
        search_button = driver.find_element(By.XPATH,
                                            "//button[contains(text(), 'Конвертировать')]"
                                            )
        search_button.click()
        # Ждем загрузки результатов поиска
        time.sleep(1)
        # Получаем HTML-код страницы после выполнения поиска
        search_results_html = driver.page_source
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(search_results_html, 'lxml')
        code = soup.find("span", class_="classifier-code okpd")
        name = soup.find("span", class_="classifier-description")
        return Okpd2Data(code=code.text, name=name.text)
    except:
        pass

    return None
