import os
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_trts_answer(product_name: str) -> str:
    trts_dict = {}
    try:
        # Получаем путь к текущей директории скрипта
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Формируем путь к исполняемому файлу драйвера
        driver_path = os.path.join(current_directory, 'chromedriver.exe')
        # Настройки для запуска Chrome в безголовом режиме
        chrome_options = Options()
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        # Переходим на сайт
        driver.get('https://сертификаты-соответствия.рус/')
        wait = WebDriverWait(driver, 7)
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ya-site-form__input-text')))
        # Находим поле ввода и вводим значение "НКУ"
        search_input = driver.find_element_by_css_selector('.ya-site-form__input-text')
        search_input.send_keys(f'{product_name}')
        # Находим кнопку поиска и нажимаем на неё
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        # Ждем загрузки результатов поиска
        # Получаем HTML-код страницы после выполнения поиска
        search_results_html = driver.page_source

        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(search_results_html, 'lxml')
        url1 = soup.find("a", class_="b-serp-item__title-link")['href']
        print('url1 = ', url1)
        driver.get(url1)
        search_results_html = driver.page_source
        soup = BeautifulSoup(search_results_html, 'lxml')
        tr_ts = soup.find_all("p", string=re.compile(r'ТР ТС'))
        for reglament in tr_ts:
            trts_dict[reglament.text] = reglament.text
        driver.quit()
        print('trts_dict = ', trts_dict)
        return trts_dict
    except:
        trts_dict['Ошибка загрузки данных. Попробуйте указать более общее название продукции.'] = ' '
        return trts_dict

