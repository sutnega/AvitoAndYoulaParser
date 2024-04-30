import json

# Sample data replaced with 'data = your_json_data' for actual use
data = {
    "Youla": [
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Мытищи",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/mytischi/ehlektronika/aksessuary/pult-657f629cbf47276d780d9714?source_view=search"
            },
            {
                "market": "Youla",
                "name": "пульт д/у LCD REMOTE",
                "city": "Мытищи",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/mytischi/ehlektronika/aksessuary/pult-du-lcd-remote-609c16d8f8146b360a3fd2c9?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт д/у DVR для видеорегистратора",
                "city": "Мытищи",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/mytischi/ehlektronika/aksessuary/pult-du-dvr-dlia-vidieorieghistratora-619cf0ae79fb5b2a7469182d?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Мытищи",
                "price": "190",
                "discount": "",
                "url": "https://youla.ru/mytischi/ehlektronika/aksessuary/pulty-5aa43197dbdf0f26251c0242?source_view=search"
            },
            {
                "market": "Youla",
                "name": "DVD",
                "city": "Мытищи",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/mytischi/ehlektronika/mediapleery/dvd-6607e76597fffd6a4802a5d4?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульты",
                "city": "Селятино",
                "price": "180",
                "discount": "",
                "url": "https://youla.ru/selyatino/ehlektronika/aksessuary/pulty-65c776749ca594a61f09a6f8?source_view=search"
            },
            {
                "market": "Youla",
                "name": "пульт",
                "city": "Люберцы",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/lyubertsy/ehlektronika/aksessuary/pult-5f081c378b54ff5291583fd7?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "50",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-5c3c7b7213a31e34b0583dd2?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/2-novykh-pulta-616fcf1168fab730192f57cb?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-62551ecc169e426c9050d621?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-65c9d7b115c5221514030704?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Электросталь",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/elektrostal/ehlektronika/aksessuary/pult-603a23c43b2d8436ab3fc16b?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-65589dd64d01b81c9203acea?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-62551ecc169e426c9050d621?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-65c9d7b115c5221514030704?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Электросталь",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/elektrostal/ehlektronika/aksessuary/pult-603a23c43b2d8436ab3fc16b?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-65589dd64d01b81c9203acea?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-60e0b5e001493e382d2ec093?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Одинцово",
                "price": "100",
                "discount": "",
                "url": "https://youla.ru/odintsovo/ehlektronika/aksessuary/pult-638861328de4a46721426d7a?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт",
                "city": "Москва",
                "price": "65",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pulty-ot-tielievizora-samsungh-5cb1ab1776bdc21b3f44b752?source_view=search"
            },
            {
                "market": "Youla",
                "name": "Пульт.",
                "city": "Москва",
                "price": "200",
                "discount": "",
                "url": "https://youla.ru/moskva/ehlektronika/aksessuary/pult-62592558e5deae7e0a77e80b?source_view=search"
            }

    ],
    "Avito": [
    {
        "market": "Avito",
        "name": "Пульт Vogele",
        "price": "0",
        "description": "Мы производим продажу и ремонт основных и боковых пультов асфальтоукладчиков Vogele Super 1800-2, 1600-2, 1900-3, а также микроконтроллеров на от асфальтоукладчика Vogele Super 1800-2, 1600-2, 1900-3 и микроконтроллеров на Фрезу Wirtgen 2000-2100, джостики, центральный дисплей: Vogele Super 1100-2. Vogele Super 1103-2. Vogele Super 1300-2. Vogele Super 1303-2. Vogele Super 1303-2. Vogele Super 1600-2. Vogele Super 1603-2. Vogele Super 1800-2. Vogele Super 1800-2 SM. Vogele Super 1800-2 SP. Vogele Super 1803-2. Vogele Super 1900-2. Vogele Super 2100-2. Vogele Super 2100-2. Vogele Super 2500. Vogele Super 600. Vogele Super 800.",
        "url": "https://www.avito.ru/moskva/zapchasti_i_aksessuary/pult_vogele_3982487137"
    },
    {
        "market": "Avito",
        "name": "Пульт ду",
        "price": "25",
        "description": "Пульт от телеприставки.",
        "url": "https://www.avito.ru/egorevsk/audio_i_video/pult_du_3861629984?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульты ду для видемагнитофона",
        "price": "0",
        "description": "Пульт управления видеомагнитофоном Шарп. Работоспособность неизвестна нет видеомагнитофона. Отдам бесплатно, самовывоз или отправлю за ваш счёт.",
        "url": "https://www.avito.ru/moskva/audio_i_video/pulty_du_dlya_videmagnitofona_2366805171"
    },
    {
        "market": "Avito",
        "name": "Пульт для ворот и шлагбаума Came,Nice,Doorhan,Faac",
        "price": "200",
        "description": "Доброго времени суток. У нас Вы можете купить пульты для ворот и шлагбаумов Came, Nice, Doorhan, Bft, Apollo, Faac, AN-Motors, Nero Radio, по самым низким ценам. Команда профессионалов поможет настроить и подобрать необходимый пульт под Вашу автоматику. Свяжитесь с нами любым удобным для Вас способом и мы подберем Вам нужную модель пульта. Наши Преимущества! Гарантия лучшей цены (напишите нам и мы предложим Вам лучшую цену на рынке). Оптовые цены. Большой опыт работы на рынке. Работаем с 2009 года! Умеем работать абсолютно с любыми пультами и автоматическими системами! (есть вопросы? Напишите нам личное сообщение в Авито и Вы получите моментальный ответ). Оперативная и Бесплатная доставка от 3-х пультов по Москве или ближайшего Вашего метро по времени. Доставка по всей России. Бесплатное программирование с пульта на пульт. Обмен или возврат нашей продукции без всяких дополнительных проверок и диагностик. Гарантия на всю продукцию. Работа с юридическими лицами. Оплата курьеру при получении. Оплата по счету ( для юридических лиц). Перевод на карту. Оплата картой. Купить Пульты Вы можете позвонив по телефону с 9:00 до 21:00 или написав в личные сообщения в Авито, мы ответим на любые вопросы. Оптовый Прайс На. Пульты для ворот и шлагбаумов. Свяжитесь с нами и мы сделаем для Вас предложение от которого Вы не сможете отказаться. Еще мы дарим подарки. Модель: Пульт Apollo Joy (Статический код 433,92mhz). — 1 шт- 500 руб. — от 5 шт- 450 руб. — от 10 шт- 400 руб. — от 20 шт- 350 руб. — от 30 шт- 300 руб. — от 45 шт- 280 руб. — от 60 шт- 250 руб. От 100 шт — по запросу. Пульт Apollo Sea (Статический код 433,92mhz). — 1 шт- 500 руб. — от 5 шт- 450 руб. — от 10 шт- 400 руб. — от 20 шт- 350 руб. — от 30 шт- 300 руб. — от 45 шт- 280 руб. — от 60 шт- 250 руб. От 100 шт — по запросу. Пульт Apollo Pro (Универсальный код заменяет 95% пультов с частотой 433.92 Mhz). — 1 шт- 600 руб. — от 5 шт- 550 руб. — от 10 шт- 500 руб. — от 20 шт- 450 руб. — от 30 шт- 400 руб. — от 45 шт- 370 руб. — от 60 шт- 350 руб. Пульт Apollo Sim Sim («Мульти» заменят 90% пультов на рынке). — 1 шт- 950 руб. — от 5 шт- 900 руб. — от 10 шт- 850 руб. — от 20 шт 800 руб. — от 30 шт- 750 руб. — от 45 шт- 700 руб. — от 60 шт- 650 руб. — от 100 шт- по запросу. Пульт Apollo Doorhan. — 1 шт- 500 руб. — от 5 шт- 450 руб. — от 10 шт- 400 руб. — от 20 шт- 390 руб. — от 30 шт- 370 руб. — от 45 шт- 360 руб. — от 60 шт- 350 руб. — от 100 шт- 300 руб. — Оптовикам цена по запросу. Пульт Came TW 2 EE (Twin 2). — 1 шт- 1600 руб. — от 5 шт- 1550 руб. — от 10 шт- 1600 руб. — от 20 шт- 1500 руб. — от 30 шт- 1480 руб. — от 45 шт- 1450 руб. — от 60 шт- 1430 руб. — от 90 шт- 1370 руб. Пульт Came TW 4 EE ( Twin 4). — 1 шт- 2200 руб. — от 5 шт- 2150 руб. — от 10 шт- 2100 руб. — от 20 шт- 2050 руб. — от 30 шт- 2000 руб. — от 45 шт- 1970 руб. — от 60 шт- 1950 руб. Пульт Nice Flo 2 RE. — 1 шт- 600 руб. — от 5 шт- 550 руб. — от 10 шт- 500 руб. — от 20 шт- 450 руб. — от 30 шт- 400 руб. Пульт Nice Flo 2 RS (Flor-s). — 1 шт- 500 руб. — от 5 шт- 480 руб. — от 10 шт- 470 руб. — от 20 шт- 450 руб. — от 30 шт- 380 руб. — опт — 360 руб. Пульт Nice Flo 4 RS (Flor-s). — 1 шт- 600 руб. — от 5 шт- 550 руб. — от 10 шт- 500 руб. — от 20 шт- 450 руб. — от 30 шт- 400 руб. Пульт Nice SM 2 (smilo). — 1 шт- 500 руб. — от 5 шт- 480 руб. — от 10 шт- 470 руб. — от 20 шт- 450 руб. — от 30 шт- 420 руб. — от 45 шт- 410 руб. — от 60 шт- 400 руб. — от 100 шт- 380 руб. Пульт Nice SM 4 (smilo). — 1 шт- 650 руб. — от 5 шт- 600 руб. — от 10 шт- 550 руб. — от 20 шт- 500 руб. — от 30 шт- 450 руб. Пульт Bft Mitto 2. — 1 шт- 500 руб. — от 5 шт- 480 руб. — от 10 шт- 470 руб. — от 20 шт- 450 руб. — от 30 шт- 420 руб. — от 45 шт- 410 руб. — от 60 шт- 400 руб. - опт 380 руб. Пульт Bft Mitto 4. — 1 шт- 650 руб. — от 5 шт- 600 руб. — от 10 шт- 550 руб. — от 20 шт- 540 руб. — от 30 шт- 520 руб. — от 45 шт- 510 руб. — от 60 шт- 500 руб. — от 100 шт- 450 руб. Пульт Doorhan 2 Pro (Transmitter). — 1 шт- 600 руб. — от 5 шт- 550 руб. — от 10 шт- 500 руб. — от 20 шт- 450 руб. — от 30 шт- 400 руб. Пульт Doorhan Transmitter 4. — 1 шт- 600 руб. — от 5 шт- 550 руб. — от 10 шт- 500 руб. — от 20 шт- 450 руб. — от 30 шт- 400 руб. Пульт faac XT 2 Slh LR. — 1 шт — 1100 руб. — от 5 шт — 1050 руб. — от 10 шт — 1000 руб. — от 20 шт — 950 руб. — от 30 шт — 900 руб. Пульт faac XT 4 Slh LR. — 1 шт — 1200 руб. — от 5 шт — 1150 руб. — от 10 шт — 1100 руб. — от 20 шт — 1050 руб. — от 30 шт — 990 руб. Пульт An-motors AT4. — 1 шт- 500 руб. — от 5 шт- 450 руб. — от 10 шт- 420руб. — от 20 шт- 400 руб. — от 30 шт- 380 руб. Пульт Alutech AT-4N. — 1 шт- 600 руб. — от 5 шт- 550 руб. — от 10 шт- 500 руб. — от 20 шт- 450руб. — от 30 шт- 400 руб. — Оптовикам цена по запросу. Пульт Nero Radio 8101-1M. — 1 шт — 1050 руб. — от 5 шт — 1000 руб. — от 10 шт — 980 руб. — от 20 шт — 950 руб. — от 30 шт — 930 руб. — от 45 шт- 900 руб. — от 60 шт- 870 руб. Пульт Nero Radio 8101-2M. — 1 шт — 800 руб. — от 5 шт — 730 руб. — от 10 шт -720 руб. — от 20 шт — 700 руб. Пульт Nero Radio 8101-4M. — 1 шт — 1250 руб. — от 5 шт — 1230руб. — от 10 шт -1200 руб. — от 20 шт — 1150 руб. — от 30 шт — 1130 руб. — от 45 шт- 1100 руб. — от 60 шт- 1050 руб. Возможно Вы искали. Пульт для ворот, брелок для шлагбаума, пульт для шлагбаума, брелок для ворот, программирование пультов для ворот, дубликат пульта для ворот, копирование пультов для ворот, ключ от шлагбаума, универсальные пульты для шлагбаумов, универсальный пульт для ворот, универсальный брелок, сделать пульт от шлагбаума.",
        "url": "https://www.avito.ru/moskva/remont_i_stroitelstvo/pult_dlya_vorot_i_shlagbauma_camenicedoorhanfaac_1281836065?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульты ду для телевизора",
        "price": "200",
        "description": "Пульт от Т V bbk.",
        "url": "https://www.avito.ru/chernogolovka/audio_i_video/pulty_du_dlya_televizora_3977626409?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульт ду samsung",
        "price": "110",
        "description": "Пульт рабочий. Продаю за ненадобнрстью.",
        "url": "https://www.avito.ru/zhukovskiy/audio_i_video/pult_du_samsung_3427236313?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульт для приставки МТС",
        "price": "200",
        "description": "Пульт от тюнера Мтс, рабочий.",
        "url": "https://www.avito.ru/moskva/audio_i_video/pult_dlya_pristavki_mts_3831597879?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульт",
        "price": "150",
        "description": "Все работают. 1 — Билайн Rasse-001 — 200р. 2 — Lumax — 150р. 3 — noname — 150р. 4 — avermedia — 150р. По всем вопросам пишите сюда. Доставка только почтой России.",
        "url": "https://www.avito.ru/davydovo/audio_i_video/pult_2647615910?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульт универсальный AT6400 (cisco/Билайн)",
        "price": "200",
        "description": "Универсальный ИК-пульт дистанционного управления AT6400 alltouch. Б/у. От ТВ-приставки. Есть несколько штук. При покупке через Авито доставку +10% к цене.",
        "url": "https://www.avito.ru/moskva/audio_i_video/pult_universalnyy_at6400_ciscobilayn_3654441057?slocation=107620"
    },
    {
        "market": "Avito",
        "name": "Пульт ду Panasonic",
        "price": "60",
        "description": "Пульт от телевизора Panasonic вроде ламповый.",
        "url": "https://www.avito.ru/moskva/audio_i_video/pult_du_panasonic_4069642608?slocation=107620"
    }
]
}

html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Listings</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
        }
        .market {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            width: calc(50% - 20px);
            overflow: hidden;
        }
        .market h3 {
            background-color: #007bff;
            color: #fff;
            margin: 0;
            padding: 10px 20px;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f8f9fa;
        }
        tr:hover {
            background-color: #f2f2f2;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
            .market {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <h1 style="text-align: center; margin-top: 20px;">Market Listings Overview</h1>
    <div class="container">
"""

html_end = """
    </div>
</body>
</html>
"""


def generate_market_div(market_name, listings):
    html_content = f"<div class='market'><h3>{market_name}</h3>"
    html_content += """
    <table>
        <tr>
            <th>Name</th>
            <th>City/Description</th>
            <th>Price</th>
            <th>URL</th>
        </tr>
    """

    for item in listings:
        name = item.get("name", "N/A")
        city_or_description = item.get("city", item.get("description", "N/A"))
        price = item.get("price", "N/A")
        url = item.get("url", "#")
        html_content += f"""
            <tr>
                <td>{name}</td>
                <td>{city_or_description}</td>
                <td>{price}</td>
                <td><a href="{url}" target="_blank">Link</a></td>
            </tr>
        """

    html_content += "</table></div>"
    return html_content


html_body = ""
for market, listings in data.items():
    html_body += generate_market_div(market, listings)

html_content = html_start + html_body + html_end

# Writing the HTML content to a file
with open("market_listings_pretty.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file 'market_listings_pretty.html' has been created successfully.")