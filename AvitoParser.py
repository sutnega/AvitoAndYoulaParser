import json

"""Selenium антидетект"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # для спрятанного хрома
from selenium.webdriver.chrome.service import Service  # Для проблем драйвера
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller   #chrome driver autoinstall
import random
import time



class AvitoParser:
    # инициализация, ссылка, ключевые слова, кол-во страниц
    def __init__(self, url: str, items: list, count: int = 10, price: int = 0, version_main=None):
        chromedriver_autoinstaller.install()
        self.url = url
        self.items = items
        self.count = count
        self.price = price
        self.version_main = version_main
        self.data = []
        self.unique_urls = []

    # передача версии Хрома
    def __set_up(self):
        #chromedriver_autoinstaller.install()
        #service = Service(executable_path="chromedriver")
        options = Options()
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        #try:

        #except Exception as e:
        self.driver = uc.Chrome(version_main=self.version_main, options=options)
        #self.driver = uc.Chrome( service=service,options=options)
    def __get_url(self):
        self.driver.get(self.url)
        time.sleep(random.uniform(10, 25))  # Случайная задержка
        # поиск кнопки с надписью "Отправить"
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Отправить']"))
            )

            # приостановка кода, пока пользователь не нажмет на кнопку
            input("Нажмите на кнопку Отправить на странице, чтобы продолжить...")
        except:
            if self.driver.find_element(By.XPATH,"//*[contains(text(), 'по запросу')]"):
                pass

        """
        if "Доступ ограничен" in self.driver.get_title():
            time.sleep(10)
            raise Exception("Перезапуск из-за блокировки IP")

        self.driver.open_new_window()  # сразу открываем и вторую вкладку
        self.driver.switch_to_window(window=0)
"""

    def __paginator(self):
        time.sleep(random.uniform(1, 3))
        while self.driver.find_elements(By.CSS_SELECTOR,
                                        "[data-marker='pagination-button/nextPage']") and self.count > 0:
            self.__parse_page()
            # нажимаем page down для прогрузки первого блока
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']").click()
            self.count -= 1


    def __parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")  # сбор контейнера товара
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR,
                                             "[class*='item-description']").text  # добавление звездочки для нечеткого класса
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute("href")
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
            data = {
                'market': 'Avito',
                'name': name,
                'price': price,
                'description': description,
                'url': url,

            }
            if price == 'Бесплатно':
                price = 0
            if url not in self.unique_urls:
                self.unique_urls.append(url)
                if self.items!=['']:
                    if any([item.lower() in description.lower() for item in self.items]) and int(price) <= self.price:
                        self.data.append(data)
                        print(data)
                elif int(price) <= self.price:
                    self.data.append(data)
                    print(data)

            # print(name, description, url, price, )
        self.__save_data()
        print('осталось страниц ' + str(self.count-1))

    def __save_data(self):
        with open("Avito.json", "w", encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def parse(self):
        chromedriver_autoinstaller.install()
        self.__set_up()
        self.__get_url()
        try:
            self.__paginator()
        except Exception as ex:
            print(f'Непредвиденная ошибка: {ex}')
            self.driver.close()
            self.driver.quit()
        self.driver.close()
        self.driver.quit()


    if __name__ == "__main__":
        url_avito = f'https://www.avito.ru/moskva_i_mo?q=пульт'
        url_avito = f'https://www.avito.ru/moskva_i_mo?q=ножницы'
        url_avito = f'https://www.avito.ru/moskva_i_mo?p={5}&q=ножницы'
        print(url_avito)
        price = 500
        print('Запуск парсера на Авито')
        from AvitoParser import AvitoParser
        try:
            AvitoParser(url=url_avito, version_main=124, count=5, price=int(price), items=[]).parse()
        except Exception as e:
            print(f"Error while parsing Avito: {e}")
            time.sleep(random.uniform(10, 30))
            try:
                time.sleep(random.uniform(10, 30))
                AvitoParser(url=url_avito, version_main=110, count=5, price=int(price), items=[]).parse()
            except Exception as e:
                print(f"Error while retrying Avito: {e}")