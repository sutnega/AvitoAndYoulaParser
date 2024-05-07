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


def input_url(minPrice, maxPrice):
    if minPrice=='':minPrice=0
    if maxPrice == '':maxPrice=1000
    minPrice=str(minPrice)
    maxPrice=str(maxPrice)
    urlYoula = 'https://youla.ru/all?attributes[price][to]=' + maxPrice + '00&attributes[price][from]=' + minPrice + '00&q=пульт'
    #urlYoula = "https://youla.ru/?q=пульт"
    urlAvito = "https://www.avito.ru/moskva_i_mo?q=пульт"
    #urlMeshok ='https://meshok.net/listing?search=пульт'
    urlMeshok = 'https://meshok.net/listing?f_p=' + minPrice + '&search=' +'пульт'+ '&to_p=' + maxPrice
    print("1.Ввести свой запрос")
    print("2.Использовать шаблон поиска")
    answer = input()
    match answer:
        case '1':
            my_request = input()
            urlAvito = 'https://www.avito.ru/moskva_i_mo?q=' + my_request
            #urlYoula = 'https://youla.ru/?q=' + my_request
            urlYoula = 'https://youla.ru/all?attributes[price][to]='+maxPrice+'00&attributes[price][from]='+minPrice+'00&q='+ my_request
            #urlMeshok = 'https://meshok.net/listing?search=' + my_request
            urlMeshok = 'https://meshok.net/listing?f_p=' + minPrice + '&search=' + my_request + '&to_p=' + maxPrice
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
    print("мин ограничение по цене")
    minPrice = int(input())
    print("макс ограничение по цене")
    maxPrice = int(input())
    url =input_url(minPrice,maxPrice)
    urlAvito = url[0]
    urlYoula = url[1]
    urlMeshok = url[2]
    count = int(input(('Ограничение по страницам на Авито:\n')))
    data_list_count = input('Сколько примерно товаров нужно найти на Юле и Мешке? (или Enter, Стандартное значение: 50):\n')
    items = input_items()
    print('Поиск на Авито начат')
    try:AvitoParser(url=urlAvito, version_main=110,  # 124 or 110
                count=count, price=maxPrice, items=items).parse()
    except Exception as e:
        AvitoParser(url=urlAvito, version_main=110,  # 124 or 110
                count=count, price=maxPrice, items=items).parse()
    print('Поиск на Авито завершен')
    print('Поиск на Юле начат')
    try:
        YoulaParser(url=urlYoula, version_main=110,  # 124 or 110
                    price=maxPrice, data_list_count=int(data_list_count)).parse()
    except Exception as e:
        YoulaParser(url=urlYoula, version_main=124,  # 124 or 110
                    price=maxPrice, data_list_count=int(data_list_count)).parse()
    print('Поиск на Юле завершен')
    print('Поиск на Мешке начат')
    try:
        MeshokParser(url=urlMeshok, version_main=110, data_list_count=int(data_list_count),  # 124 or 110
                     price=maxPrice).parse()
    except Exception as e: \
            MeshokParser(url=urlMeshok, version_main=124, data_list_count=int(data_list_count),  # 124 or 110
                         price=maxPrice).parse()
    print('Поиск на Мешке завершен')


    from subprocess import Popen
    Popen('python VisualCreator.py')
