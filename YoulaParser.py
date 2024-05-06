import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
# pip install chromedriver-autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # для спрятанного хрома


# pip install openpyxl


class YoulaParser:
    def __init__(self, url: str, data_list_count: int, price: int = 0,
                 version_main=None):  # items: list, count: int = 10,
        self.url = url
        # self.items = items
        # self.count = count
        self.price = price
        self.version_main = version_main
        self.data = []
        self.data_list_count = data_list_count

    def __get_url(self):
        self.driver.get(self.url)

    def __set_up(self):
        chromedriver.install()
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--log-level=3')
        self.driver = uc.Chrome(version_main=self.version_main, options=options)

    def __parse_page(self, html):
        """Функция сбора данных с прогружаемой страницы"""
        soup = BeautifulSoup(html, 'html.parser')
        blocks = soup.find_all('div', {"data-test-component": "ProductOrAdCard"})
        data_list = []
        for block in blocks:
            try:
                name = block.find('span', {'data-test-block': "ProductName"}).text
            except:
                name = 'нет названия'
            try:
                city = block.find('div', {'data-test-component': "Badges"}).text.split('%')[-1]
            except:
                city = 'город не указан'
            try:
                discount = block.find('div', {'data-test-component': "Badges"}).text
                if '%' in discount:
                    discount = discount.split('%')[0]
                else:
                    discount = ''
            except:
                discount = ''
            try:
                price = block.find('p', {'data-test-block': "ProductPrice"}).text.replace('₽руб.', '') \
                    .replace('\xa0', '')
                price = price.replace(' ', '').replace('\u205f', '')
            except:
                price = 'нет цены'
            try:
                link = "https://youla.ru" + block.find('div').find('span').find('a').get('href')
            except:
                link = 'ссылка не найдена'

            if 'нет названия' in name:
                pass
            else:
                # print(name)
                # print(city)
                # print(price)
                # print(discount)
                # print(link)
                # print('-----------')
                if price == 'Бесплатно':
                    price=0
                if int(price) <= self.price:
                    description = self.__get_description(link).replace('ПоделитьсяПожаловаться на объявление', '')
                    description = description.replace('Показать на карте ↓', ' ').replace('Описание', ' Описание: ')
                    description = description.replace('Узнайте большеПоказать номерНаписать продавцу',' ')
                    description = description.replace('В избранном',' В избранном: ')
                    description = description.replace('Просмотры',' Просмотры: ')
                    description = description.replace('Размещено',' Размещено: ')
                    description = description.replace('Местоположение',' Местоположение: ')
                    description = description.replace('Категория',' Категория: ')
                    description = description.replace('Подкатегория',' Подкатегория: ')
                    description = description.replace('Тип',' Тип: ')

                    data_list.append({
                        'name': name,
                        'city': city,
                        'description':description,
                        'price': price,
                        'discount': discount,
                        'link': link
                    })
                    data = {
                        'market': 'Youla',
                        'name': name,
                        'city': city,
                        'description': description,
                        'price': price,
                        'discount': discount,
                        'url': link

                    }
                    self.data.append(data)
        self.__save_data()
        return data_list

    def __parser(self, url, data_list_count):
        """Основная функция, сам парсер"""

        try:
            self.driver.get(url)
            time.sleep(2)
            # находим высоту прокрутки
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            # нажимаем page down для прогрузки первого блока
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            data_list_pages = []
            while True:
                data_list_pages.extend(self.__parse_page(self.driver.page_source))

                # скролим один раз
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Ждем прогрузки страницы
                time.sleep(2)

                # Вычисляем новую высоту прокрутки и сравниваем с последней высотой прокрутки
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if data_list_count == '':
                    data_list_count = 1000
                if new_height == last_height:
                    break
                last_height = new_height
                print(f'Собрано {len(data_list_pages)} позиций')
                # проверка на количество выдачи
                if len(data_list_pages) >= int(data_list_count):
                    break
            return data_list_pages
        finally:
            print("завершение поиска на Юле")
            pass

        """except Exception as ex:
            print(f'Непредвиденная ошибка: {ex}')
            self.driver.close()
            self.driver.quit()
        self.driver.close()
        self.driver.quit()"""

    def __get_description(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)  # Wait for the page to load
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            description_element = soup.select_one("[data-test-component='ProductDetails']")
            if description_element:
                description = description_element.text.strip()
                return description
            else:
                return "Description not found"
        except Exception as e:
            print(f"Error while scraping description: {e}")
            return None

    def __save_data(self):
        with open("Youla.json", "w", encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def parse(self):
        self.__set_up()
        self.__get_url()
        data = self.__parser(self.url, self.data_list_count)



