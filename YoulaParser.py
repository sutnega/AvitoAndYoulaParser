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

import re  # Импорт для избавления от смайликов


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
        self.unique_urls=[]
        self.data_list_count = data_list_count

    def __get_url(self):
        self.driver.get(self.url)

    def __set_up(self):
        chromedriver.install()
        options = Options()
        #options.add_argument('--headless')
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
                url = "https://youla.ru" + block.find('div').find('span').find('a').get('href')
            except:
                url = 'ссылка не найдена'

            if 'нет названия' in name:
                pass
            else:
                # print(name)
                # print(city)
                # print(price)
                # print(discount)
                # print(url)
                # print('-----------')
                if price == 'Бесплатно':
                    price=0
                if url not in self.unique_urls:
                    self.unique_urls.append(url)
                    if int(price) <= self.price:
                        #description = self.__get_description(url).replace('ПоделитьсяПожаловаться на объявление', '')
                        description = 'not chosen'


                        data_list.append({
                            'name': name,
                            'city': city,
                            'description':description,
                            'price': price,
                            'discount': discount,
                            'url': url
                        })
                        data = {
                            'market': 'Youla',
                            'name': name,
                            'city': city,
                            'description': description,
                            'price': price,
                            'discount': discount,
                            'url': url

                        }
                        self.data.append(data)
        self.__save_data()
        return data_list

    def __parser(self, url, data_list_count):
        """Основная функция, сам парсер"""

        try:
            self.driver.get(url)
            time.sleep(2)

            try:
                # Нажать на кнопку с data-test-action="SelectGeolocationClick"
                button_geo = self.driver.find_element(By.XPATH, '//button[@data-test-action="SelectGeolocationClick"]')
                button_geo.click()
                time.sleep(2)  # пауза, чтобы страница успела обработать действие

                # Нажать на span с текстом "Город"
                span_city = self.driver.find_element(By.XPATH, '//span[text()="Город"]')
                span_city.click()
                time.sleep(2)  # пауза, чтобы страница успела обработать действие

                # Нажать на div с текстом "Москва"
                div_moscow = self.driver.find_element(By.XPATH, '//div[text()="Москва"]')
                div_moscow.click()
                time.sleep(2)  # пауза, чтобы страница успела обработать действие
                self.driver.get(url)
            except Exception as e:
                print(f"Ошибка при клике на элемент: {e}")


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
                    data_list_count = 50
                if new_height == last_height:
                    break
                last_height = new_height
                print(f'Собрано {len(data_list_pages)} позиций')
                # проверка на количество выдачи
                if len(self.unique_urls) >= int(data_list_count):
                    break
            return data_list_pages
        finally:
            print("завершение поиска на Юле")
            pass


    def __get_description(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)  # Wait for the page to load
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            description_element = soup.select_one("[data-test-component='ProductDetails']")
            if description_element:
                description = description_element.text.strip()
                # Удаление эмодзи и других специальных символов
                #description = re.sub(r"[^а-яА-ЯёЁ ,.!?;:()\"\'-]", '', description)  # фильтрация Unicode для эмодзи
                return description
            else:
                return "Description not found"
        except Exception as e:
            print(f"Error while scraping description: {e}")
            return None

    def __write_descriptions(self):
        # Путь к исходному файлу
        input_filename = 'Youla.json'
        # Путь к файлу для сохранения изменённых данных
        output_filename = 'Youla_descriptions.json'
        # Считываем данные из исходного JSON-файла
        with open(input_filename, 'r', encoding='utf-8-sig') as file:
            Youladata = json.load(file)
        # Обрабатываем каждый элемент в массиве
        for item in Youladata:
            # Извлекаем URL и выводим его
            url = item.get('url')
            description = self.__get_description(url).replace('ПоделитьсяПожаловаться на объявление', '')
            description = description.replace('Показать на карте ↓', ' ').replace('Описание', ' Описание: ')
            description = description.replace('Узнайте большеПоказать номерНаписать продавцу', ' ')
            description = description.replace('В избранном', ' В избранном: ')
            description = description.replace('Просмотры', ' Просмотры: ')
            description = description.replace('Размещено', ' Размещено: ')
            description = description.replace('Местоположение', ' Местоположение: ')
            description = description.replace('Категория', ' Категория: ')
            description = description.replace('Подкатегория', ' Подкатегория: ')
            description = description.replace('Тип', ' Тип: ').replace('\u20bd', '').replace('\xd7', '')
            description = description.replace('Показать на карте', '').replace('\u2193', '').replace(' ', '')
            description = re.sub(r"[^\w\s,.!?;:()\'\"-]+", '', description, flags=re.UNICODE)
            print("Modified descr:", description)
            # Обновляем description в объекте
            item['description'] = description
        # Сохраняем изменённые данные в новый файл
        with open(output_filename, 'w') as file:
            json.dump(Youladata, file,ensure_ascii=False, indent=4)

        print(f"Modified data has been saved to {output_filename}")
    pass

    def __save_data(self):
        with open("Youla.json", "w", encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def parse(self):
        self.__set_up()
        self.__get_url()
        try:
            data = self.__parser(self.url, self.data_list_count)
            self.__write_descriptions()
        except Exception as ex:
            print(f'Непредвиденная ошибка: {ex}')
            self.driver.close()
            self.driver.quit()
        self.driver.close()
        self.driver.quit()


    if __name__ == "__main__":
        urlYoula = 'https://youla.ru/all?q=гантели'
        print(urlYoula)
        price = 500
        print('Запуск парсера на Юле')
        data_list_count = int(input('Сколько примерно товаров нужно найти? (Стандарт:50)\n'))
        from YoulaParser import YoulaParser
        try:
            YoulaParser(url=urlYoula, version_main=110,  # 124 or 110
                        price=price, data_list_count=int(data_list_count)).parse()
        except Exception as e:
            YoulaParser(url=urlYoula, version_main=124,  # 124 or 110
                        price=price, data_list_count=int(data_list_count)).parse()