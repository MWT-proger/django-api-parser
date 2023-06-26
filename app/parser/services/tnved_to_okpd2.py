import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def convert_tnved_to_okpd2(tnved_code: str) -> dict:
    try:
        okpd2_code_dict = {}
        # Получаем путь к текущей директории скрипта
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Формируем путь к исполняемому файлу драйвера
        driver_path = os.path.join(current_directory, 'chromedriver.exe')
        # Настройки для запуска Chrome в безголовом режиме
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # Запускаем браузер с заданными настройками
        driver = webdriver.Chrome(executable_path=driver_path,
                                  options=chrome_options,
                                  )
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
        okpd2_code_dict[code.text] = name.text
        print('ОКПД2= ', okpd2_code_dict)
        driver.quit()
        return okpd2_code_dict
    except:
        okpd2_code_dict = {}
        okpd2_code_dict['Ошибка загрузки.'] = ' Попробуйте позже.'
        return okpd2_code_dict

