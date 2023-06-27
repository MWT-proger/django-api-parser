from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def set_chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


class DriverChromeManager:

    def __init__(self):
        self.drever = webdriver.Chrome(options=set_chrome_options())

    def __enter__(self):
        return self.drever

    def __exit__(self, *args):
        self.drever.close()
