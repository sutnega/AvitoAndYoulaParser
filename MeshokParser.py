import json
import re

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


class MeshokParser:
    def __init__(self, url: str, data_list_count: int, price: int = 0,
                 version_main=None):  # items: list, count: int = 10,
        self.url = url
        # self.items = items
        # self.count = count
        self.price = price
        self.version_main = version_main
        self.data = []
        self.unique_links =[]
        self.data_list_count = data_list_count
        self.numberOfItems = data_list_count

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
        blocks = soup.find_all('div', {"class": "itemCardList_743f6"})
        #print("soup blocks")
        #print(blocks)
        print("__" * 100)

        #blocks = self.driver.find_elements(By.CLASS_NAME, "itemCardList_743f6")
        #print("driver blocks:")
        #print(blocks)
        data_list = []
        for block in blocks:
            try:
                name = block.find('div', {'class': "itemTitle_743f6"}).text
            except:
                name = 'нет названия'
            try:
                city = block.find('div', {'data-test-component': "Badges"}).text.split('%')[-1]
            except:
                city = 'город не указан'
            try:
                price = block.find('div', {'class': "priceAndIcons_35695"}).text.replace('₽руб.', '') \
                    .replace('\xa0', '').replace(' ', '')
                price = price.replace('\u205f', '').replace('₽', '').replace('Благотворительныйлот', '')
                price = price.replace(',', '.')
            except:
                price = 'нет цены'
            try:
                link = "https://meshok.net" + block.find('a').get('href')
            except:
                link = 'ссылка не найдена'

            if 'нет названия' in name:
                pass
            else:
                print(name)
                # print(city)
                print(price)
                print(link)
                # print('-----------')
                if price == 'Бесплатно':
                    price = 0
                if link not in self.unique_links:
                    self.unique_links.append(link)
                    if price!='нет цены':
                        if int(round(float(price))) <= self.price :
                            #description = self.__get_description(link).replace('ПоделитьсяПожаловаться на объявление', '')
                            description = 'not chosen'
                            description = description.replace(' ', ' ').replace(' ', ' ').replace(' ', ' ')

                            data_list.append({
                                'name': name,
                                'city': city,
                                'description': description,
                                'price': price,
                                'link': link
                            })
                            data = {
                                'market': 'Meshok',
                                'name': name,
                                'city': city,
                                'description': description,
                                'price': price,
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
                    data_list_count = 50
                if new_height == last_height:
                    break
                last_height = new_height
                print(f'Собрано {len(data_list_pages)} позиций')
                # проверка на количество выдачи
                if len(self.unique_links) >= int(data_list_count):
                    break
            return data_list_pages
        finally:
            print("завершение поиска на Мешке")
            pass

    def __get_description(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)  # Wait for the page to load
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            description_element = soup.select_one("[itemprop='description']")
            if description_element:
                description = description_element.text.strip()
                return description
            else:
                return "Description not found"
        except Exception as e:
            print(f"Error while scraping description: {e}")
            return None
    def __write_descriptions(self):
        # Путь к исходному файлу
        input_filename = 'Meshok.json'
        # Путь к файлу для сохранения изменённых данных
        output_filename = 'Meshok_descriptions.json'
        # Считываем данные из исходного JSON-файла
        with open(input_filename, 'r', encoding='utf-8-sig') as file:
            Meshokdata = json.load(file)
        # Обрабатываем каждый элемент в массиве
        for item in Meshokdata:
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
            description = description.replace(' ', ' ').replace(' ', ' ').replace(' ', ' ')
            description = re.sub(r"[^\w\s,.!?;:()\'\"-]+", '', description, flags=re.UNICODE)
            print("Modified descr:", description)
            # Обновляем description в объекте
            item['description'] = description
        # Сохраняем изменённые данные в новый файл
        with open(output_filename, 'w') as file:
            json.dump(Meshokdata, file,ensure_ascii=False, indent=4)

        print(f"Modified data has been saved to {output_filename}")
    pass

    def __save_data(self):
        with open("Meshok.json", "w", encoding='utf-8') as f:
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
        url = 'https://meshok.net/listing?search=пульт'
        print(url)
        print('Запуск парсера на Мешке')
        data_list_count = int(input('Сколько примерно товаров нужно найти? (Стандарт:50)\n'))
        from MeshokParser import MeshokParser
        try: MeshokParser(url=url, version_main=110,data_list_count=data_list_count, # 124 or 110
                  price=1000).parse()
        except Exception as e:\
            MeshokParser(url=url, version_main=124,data_list_count=data_list_count, # 124 or 110
                  price=1000).parse()