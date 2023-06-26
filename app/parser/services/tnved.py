import time
from typing import List

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

class TnvedData:
    def __init__(self, number:str, name:str):
        self.number = number
        self.name = name



def get_tnved_code(product_name: str, driver) -> List[TnvedData]:
    tnvedDataList = []
    try:

        driver.get('https://tnved.info/')
        # Находим поле ввода и вводим значение "НКУ"
        search_input = driver.find_element(By.ID, 'searchValue')
        search_input.send_keys(f'{product_name}')
        # Находим кнопку поиска и нажимаем на неё
        search_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Поиск')]"
        )
        search_button.click()
        # Ждем загрузки результатов поиска
        time.sleep(1)
        # Получаем HTML-код страницы после выполнения поиска
        search_results_html = driver.page_source
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(search_results_html, 'lxml')
        codes = soup.find_all(
            "a",
            class_=("MuiTypography-root MuiTypography-inherit "
                    "MuiLink-root MuiLink-underlineHover css-wp0at3")
        )
        names = soup.find('tbody', class_="MuiTableBody-root css-1xnox0e").find_all(
            class_="MuiTypography-root MuiTypography-body2 css-10x1jud")

        for code, name in zip(codes, names):
            tnvedDataList.append(TnvedData(number=code.text, name=name.text))

    except:
        pass

    return tnvedDataList
