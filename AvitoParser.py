import json

"""Selenium антидетект"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # для спрятанного хрома




class AvitoParser:
    # инициализация, ссылка, ключевые слова, кол-во страниц
    def __init__(self, url: str, items: list, count: int = 10, price: int = 0, version_main=None):
        self.url = url
        self.items = items
        self.count = count
        self.price = price
        self.version_main = version_main
        self.data = []

    # передача версии Хрома
    def __set_up(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = uc.Chrome(version_main=self.version_main, options=options)

    def __get_url(self):
        self.driver.get(self.url)

    def __paginator(self):
        while self.driver.find_elements(By.CSS_SELECTOR,
                                        "[data-marker='pagination-button/nextPage']") and self.count > 0:
            self.__parse_page()
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
                'name': name,
                'description': description,
                'url': url,
                'price': price

            }
            if price == 'Бесплатно':
                price = 0
            if self.items!=['']:
                if any([item.lower() in description.lower() for item in self.items]) and int(price) <= self.price:
                    self.data.append(data)
                    print(data)
            elif int(price) <= self.price:
                self.data.append(data)
                print(data)

            # print(name, description, url, price, )
        self.__save_data()
        print('страница' + str(self.count))

    def __save_data(self):
        with open("items.json", "w", encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def parse(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()