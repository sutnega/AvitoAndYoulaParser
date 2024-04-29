from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
#pip install chromedriver-autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # для спрятанного хрома


# pip install openpyxl


class YoulaParser:
    def __init__(self, url: str, data_list_count:int, version_main=None):  # items: list, count: int = 10, price: int = 0
        self.url = url
        # self.items = items
        # self.count = count
        # self.price = price
        self.version_main = version_main
        self.data = []
        self.data_list_count=data_list_count
    def __get_url(self):
        self.driver.get(self.url)
    def __set_up(self):
        chromedriver.install()
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--log-level=3')
        self.driver = uc.Chrome(version_main=self.version_main, options=options)

    def __get_content_page(self, html):
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
                price = block.find('p', {'data-test-block': "ProductPrice"}).text.replace('₽руб.', '').replace('\xa0',
                                                                                                               '')
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

                data_list.append({
                    'name': name,
                    'city': city,
                    'price': price,
                    'discount': discount,
                    'link': link
                })
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
                data_list_pages.extend(self.__get_content_page(self.driver.page_source))

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
            print("увы")
            pass

        """except Exception as ex:
            print(f'Непредвиденная ошибка: {ex}')
            self.driver.close()
            self.driver.quit()
        self.driver.close()
        self.driver.quit()"""

    def __save_exel(self, data):
        """Функция сохранения в файл"""
        dataframe = pandas.DataFrame(data)
        writer = pandas.ExcelWriter(f'data_yula.xlsx')
        dataframe.to_excel(writer, 'data_yula')
        writer._save()
        print(f'Сбор данных завершен. Данные сохранены в файл "data_yula.xlsx"')

    def parse(self):
        self.__set_up()
        self.__get_url()
        data = self.__parser(self.url, self.data_list_count)
        self.__save_exel(data)


if __name__ == "__main__":
    url = input(
        'Введите ссылку на раздел, с заранее выбранными характеристиками (ценовой диапазон, сроки размещения и тд):\n')
    print('Запуск парсера...')
    YoulaParser(url=url, version_main=110,data_list_count=data_list_count  # 124 or 110
                ).parse()
