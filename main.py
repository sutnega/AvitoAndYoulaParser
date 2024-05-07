"""pip install undetected-chromedriver"""
import json

"""Selenium антидетект"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # для спрятанного хрома
from AvitoParser import AvitoParser
from YoulaParser import YoulaParser
from MeshokParser import MeshokParser
#pip install chromedriver-autoinstaller
import chromedriver_autoinstaller as chromedriver


def input_url():
    urlYoula = "https://youla.ru/?q=пульт"
    urlAvito = "https://www.avito.ru/moskva_i_mo?q=пульт"
    urlMeshok ='https://meshok.net/listing?search=пульт'
    print("1.Ввести свой запрос")
    print("2.Использовать шаблон поиска")
    answer = input()
    match answer:
        case '1':
            my_request = input()
            urlAvito = 'https://www.avito.ru/moskva_i_mo?q=' + my_request
            urlYoula = 'https://youla.ru/?q=' + my_request
            urlMeshok = 'https://meshok.net/listing?search=' + my_request
            print(urlAvito)
            print(urlYoula)
            print(urlMeshok)
            return urlAvito, urlYoula, urlYoula
        case '2':
            print(urlAvito)
            print(urlYoula)
            print(urlMeshok)
            return urlAvito, urlYoula, urlMeshok
        case _:
            pass


def input_items():
    print('введите ключевые слова через запятую')
    items = (input().split(", "))
    return (items)


if __name__ == "__main__":
    chromedriver.install()
    url =input_url()
    urlAvito = url[0]
    urlYoula = url[1]
    urlMeshok = url[2]
    count = int(input(('Ограничение по страницам на Авито:\n')))
    data_list_count = input('Сколько примерно товаров нужно найти на Юле и Мешке? (или Enter, Стандартное значение: 50):\n')
    print("макс ограничение по цене")
    price = int(input())
    items = input_items()
    print('Поиск на Авито начат')
    try:AvitoParser(url=urlAvito, version_main=110,  # 124 or 110
                count=count, price=price, items=items).parse()
    except Exception as e:
        AvitoParser(url=urlAvito, version_main=110,  # 124 or 110
                count=count, price=price, items=items).parse()
    print('Поиск на Авито завершен')
    print('Поиск на Юле начат')
    try:
        YoulaParser(url=urlYoula, version_main=110,  # 124 or 110
                    price=price, data_list_count=int(data_list_count)).parse()
    except Exception as e:
        YoulaParser(url=urlYoula, version_main=124,  # 124 or 110
                    price=price, data_list_count=int(data_list_count)).parse()
    print('Поиск на Юле завершен')
    print('Поиск на Мешке начат')
    try:
        MeshokParser(url=urlMeshok, version_main=110, data_list_count=int(data_list_count),  # 124 or 110
                     price=price).parse()
    except Exception as e: \
            MeshokParser(url=urlMeshok, version_main=124, data_list_count=int(data_list_count),  # 124 or 110
                         price=price).parse()
    print('Поиск на Мешке завершен')


    from subprocess import Popen
    Popen('python VisualCreator.py')
