import tkinter as tk
from tkinter import ttk
import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from AvitoParser import AvitoParser
from YoulaParser import YoulaParser
from MeshokParser import MeshokParser
import chromedriver_autoinstaller as chromedriver
from subprocess import Popen


class ParserInputApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Поиск на интернет-площадках")
        self.geometry("600x600")  # Увеличил высоту окна

        # Variables
        self.min_price = tk.StringVar(value="0")
        self.max_price = tk.StringVar(value="1000")
        self.count_avito = tk.StringVar(value="3")
        self.data_list_count = tk.StringVar(value="50")
        self.search_query = tk.StringVar(value="пульт")
        self.items = tk.StringVar(value="пульт")
        self.blacklist = tk.StringVar(value="сломан")

        # Parser selection
        self.run_avito = tk.BooleanVar(value=True)
        self.run_youla = tk.BooleanVar(value=True)
        self.run_meshok = tk.BooleanVar(value=True)
        self.need_description = tk.BooleanVar(value=False)  # Новый чекбокс

        # Create Inputs
        self.create_text_input("Минимальная цена:", self.min_price, 0)
        self.create_text_input("Максимальная цена:", self.max_price, 1)
        self.create_text_input("Ограничение страниц Авито:", self.count_avito, 2)
        self.create_text_input("Ограничение товаров Юла и Мешок:", self.data_list_count, 3)
        self.create_text_input("Поисковой запрос:", self.search_query, 4)
        self.create_text_input("Ключевые слова (через запятую):", self.items, 5)
        self.create_text_input("Черный список слов (через запятую):", self.blacklist, 6)

        # Parser selection checkboxes
        self.create_parser_checkbox("Запустить поиск на Avito :", self.run_avito, 7)
        self.create_parser_checkbox("Запустить поиск на Youla Parser:", self.run_youla, 8)
        self.create_parser_checkbox("Запустить поиск на Meshok:", self.run_meshok, 9)
        self.create_parser_checkbox("Нужны описания товаров:", self.need_description, 10)  # Новый чекбокс

        # Submit button
        submit_button = ttk.Button(self, text="Запустить поиск", command=self.start_parsing)
        submit_button.grid(row=11, column=1, pady=10)
        # Button to run VisualCreator.py script
        visual_creator_button = ttk.Button(self, text="Вывести результаты", command=self.run_visual_creator)
        visual_creator_button.grid(row=12, column=1, pady=10)

    def create_text_input(self, label_text, variable, row):
        """Creates a labeled text input field."""
        label = ttk.Label(self, text=label_text)
        label.grid(row=row, column=0, pady=5, padx=10, sticky="w")
        entry = ttk.Entry(self, textvariable=variable)
        entry.grid(row=row, column=1, pady=5, padx=10)

    def create_parser_checkbox(self, label_text, variable, row):
        """Creates a parser selection checkbox."""
        checkbox = ttk.Checkbutton(self, text=label_text, variable=variable)
        checkbox.grid(row=row, column=1, pady=5, padx=10, sticky="w")

    def start_parsing(self):
        """Starts the parsing process with the provided input values."""
        chromedriver.install()

        min_price = self.min_price.get()
        max_price = self.max_price.get()
        count_avito = int(self.count_avito.get())
        data_list_count = self.data_list_count.get()
        search_query = self.search_query.get()
        items = [item.strip() for item in self.items.get().split(",")]
        blacklist = [black_word.strip() for black_word in self.blacklist.get().split(",")]
        need_description = self.need_description.get()  # Получаем значение нового чекбокса

        if not min_price: min_price = "0"
        if not max_price: max_price = "1000"
        if not data_list_count: data_list_count = "50"

        url_avito, url_youla, url_meshok = self.generate_urls(min_price, max_price, search_query)

        print(f"Avito URL: {url_avito}")
        print(f"Youla URL: {url_youla}")
        print(f"Meshok URL: {url_meshok}")

        if self.run_avito.get():
            self.run_avito_parser(url_avito, count_avito, max_price, items)

        if self.run_youla.get():
            self.run_youla_parser(url_youla, data_list_count, max_price, need_description, blacklist)

        if self.run_meshok.get():
            self.run_meshok_parser(url_meshok, data_list_count, max_price, need_description, blacklist)

        print("Parsing completed.")

    def generate_urls(self, min_price, max_price, search_query):
        """Generate URLs for different platforms."""
        url_youla = f'https://youla.ru/all?attributes[price][to]={max_price}00&attributes[price][from]={min_price}00&q={search_query}'
        url_avito = f'https://www.avito.ru/moskva_i_mo?q={search_query}'
        url_meshok = f'https://meshok.net/listing?f_p={min_price}&search={search_query}&to_p={max_price}'
        return url_avito, url_youla, url_meshok

    def run_avito_parser(self, url, count, max_price, items):
        """Run Avito parser with provided parameters."""
        try:
            AvitoParser(url=url, version_main=110, count=count, price=int(max_price), items=items).parse()
        except Exception as e:
            print(f"Error while parsing Avito: {e}")
            try:
                AvitoParser(url=url, version_main=124, count=count, price=int(max_price), items=items).parse()
            except Exception as e:
                print(f"Error while retrying Avito: {e}")

    def run_youla_parser(self, url, data_list_count, max_price, need_description, blacklist):
        """Run Youla parser with provided parameters."""
        try:
            YoulaParser(url=url, version_main=110, price=int(max_price), data_list_count=int(data_list_count),
                        need_description=need_description, blacklist=blacklist).parse()
        except Exception as e:
            print(f"Error while parsing Youla: {e}")
            try:
                YoulaParser(url=url, version_main=124, price=int(max_price), data_list_count=int(data_list_count),
                            need_description=need_description, blacklist=blacklist).parse()
            except Exception as e:
                print(f"Error while retrying Youla: {e}")

    def run_meshok_parser(self, url, data_list_count, max_price, need_description, blacklist):
        """Run Meshok parser with provided parameters."""
        try:
            print("Начинаю поиск на Мешке")
            MeshokParser(url=url, version_main=110, data_list_count=int(data_list_count), price=int(max_price),
                         need_description=need_description, blacklist=blacklist).parse()
        except Exception as e:
            print(f"Error while parsing Meshok: {e}")
            try:
                print("Перезапускаем поиск на Мешке")
                MeshokParser(url=url, version_main=124, data_list_count=int(data_list_count), price=int(max_price),
                             need_description=need_description, blacklist=blacklist).parse()
            except Exception as e:
                print(f"Error while retrying Meshok: {e}")

    def run_visual_creator(self):
        """Runs the VisualCreator.py script."""
        need_description = self.need_description.get()
        try:
            from VisualCreator import visualize
            visualize(need_description=need_description)
            """Popen(['python', 'VisualCreator.py'])
            print("VisualCreator.py script started.")"""
        except Exception as e:
            print(f"Failed to start VisualCreator.py: {e}")


if __name__ == "__main__":
    app = ParserInputApp()
    # from subprocess import Popen
    # Popen('python VisualCreator.py')
    app.mainloop()
