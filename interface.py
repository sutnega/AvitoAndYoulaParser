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


class ParserInputApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Parser Input Variables")
        self.geometry("600x550")

        # Variables
        self.min_price = tk.StringVar(value="0")
        self.max_price = tk.StringVar(value="1000")
        self.count_avito = tk.StringVar(value="3")
        self.data_list_count = tk.StringVar(value="50")
        self.search_query = tk.StringVar(value="пульт")
        self.items = tk.StringVar(value="пульт")

        # Parser selection
        self.run_avito = tk.BooleanVar(value=True)
        self.run_youla = tk.BooleanVar(value=True)
        self.run_meshok = tk.BooleanVar(value=True)

        # Create Inputs
        self.create_text_input("Min Price:", self.min_price, 0)
        self.create_text_input("Max Price:", self.max_price, 1)
        self.create_text_input("Avito Page Limit:", self.count_avito, 2)
        self.create_text_input("Youla & Meshok Item Limit:", self.data_list_count, 3)
        self.create_text_input("Search Query:", self.search_query, 4)
        self.create_text_input("Items (comma-separated):", self.items, 5)

        # Parser selection checkboxes
        self.create_parser_checkbox("Run Avito Parser:", self.run_avito, 6)
        self.create_parser_checkbox("Run Youla Parser:", self.run_youla, 7)
        self.create_parser_checkbox("Run Meshok Parser:", self.run_meshok, 8)

        # Submit button
        submit_button = ttk.Button(self, text="Start Parsing", command=self.start_parsing)
        submit_button.grid(row=9, column=1, pady=10)

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
            self.run_youla_parser(url_youla, data_list_count, max_price)

        if self.run_meshok.get():
            self.run_meshok_parser(url_meshok, data_list_count, max_price)

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
                AvitoParser(url=url, version_main=110, count=count, price=int(max_price), items=items).parse()
            except Exception as e:
                print(f"Error while retrying Avito: {e}")

    def run_youla_parser(self, url, data_list_count, max_price):
        """Run Youla parser with provided parameters."""
        try:
            YoulaParser(url=url, version_main=110, price=int(max_price), data_list_count=int(data_list_count)).parse()
        except Exception as e:
            print(f"Error while parsing Youla: {e}")
            try:
                YoulaParser(url=url, version_main=124, price=int(max_price), data_list_count=int(data_list_count)).parse()
            except Exception as e:
                print(f"Error while retrying Youla: {e}")

    def run_meshok_parser(self, url, data_list_count, max_price):
        """Run Meshok parser with provided parameters."""
        try:
            MeshokParser(url=url, version_main=110, data_list_count=int(data_list_count), price=int(max_price)).parse()
        except Exception as e:
            print(f"Error while parsing Meshok: {e}")
            try:
                MeshokParser(url=url, version_main=124, data_list_count=int(data_list_count), price=int(max_price)).parse()
            except Exception as e:
                print(f"Error while retrying Meshok: {e}")


if __name__ == "__main__":
    app = ParserInputApp()
    from subprocess import Popen
    Popen('python VisualCreator.py')
    app.mainloop()