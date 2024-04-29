"""pip install undetected-chromedriver"""
import json

"""Selenium антидетект"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # для спрятанного хрома
from AvitoParser import AvitoParser
from YoulaParser import YoulaParser

GLOBAL_PRICE = 0




def input_url():
    urlYoula = "https://youla.ru/?q=пульт"
    urlAvito = "https://www.avito.ru/moskva_i_mo?q=пульт"
    print("1.Ввести свой запрос")
    print("2.Использовать дефолт юрл")
    answer = input()
    match answer:
        case '1':
            my_request = input()
            urlAvito = 'https://www.avito.ru/moskva_i_mo?q=' + my_request
            urlYoula = 'https://youla.ru/?q=' + my_request
            print(urlAvito)
            print(urlYoula)
            return urlAvito, urlYoula
        case '2':
            print(urlAvito)
            print(urlYoula)
            return urlAvito, urlYoula
        case _:
            pass


def input_items():
    print('введите ключевые слова через запятую')
    items = []
    items = (input().split(", "))
    return (items)


if __name__ == "__main__":
    url =input_url()
    urlAvito = url[0]
    urlYoula = url[1]
    print("Ограничение по страницам")
    count = int(input())
    print("макс ограничение по цене")
    price = int(input())
    items = input_items()
    #AvitoParser(url=urlAvito, version_main=124,  # 124 or 110
    #            count=count, price=price, items=items).parse()
    YoulaParser(url=urlYoula, version_main=124,  # 124 or 110
               count=count, price=price, items=items).parse()
