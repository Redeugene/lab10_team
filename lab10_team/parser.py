from time import sleep
from requests import get
from bs4 import BeautifulSoup
from random import randint
from random import choice
import pandas as pd




with open('proxies.txt') as file:
    proxies = file.read().splitlines()


with open('useragents.txt') as file:
    useragents = file.read().splitlines()


headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.228.0 Safari/537.36'})


def convert_to_float(df_field):
    return df_field.astype('float32')


def save_in_df(products):
    df = pd.DataFrame(columns =    ["title",
                                    "category",
                                    "price",
                                    "discount_price",
                                    "link",
                                    "site",
                                    "catalog",
                                    "stock",
                                    "stock_name",
                                    "article",
                                    "unit",
                                    "order",
                                    "inventory",
                                    "city",
                                    "price_2",
                                    "discount_price_2",
                                    "unit_2"])

    for prod in products:
        a_series = pd.Series(prod, index = df.columns)
        df = df.append(a_series, ignore_index=True)

    df["price"] = convert_to_float(df["price"])
    df["discount_price"] = convert_to_float(df["discount_price"])
    df["price_2"] = convert_to_float(df["price_2"])
    df["discount_price_2"] = convert_to_float(df["discount_price_2"])
    df = df.fillna("-1")
    df.to_csv("lerua.csv", index=False, mode='a', header=False, encoding='utf-8')


def parse_page(link):
    r = get(link, headers={'User-Agent': choice(useragents)}, proxies={'http': 'http://' + choice(proxies)})
    # print(link)
    page_html = BeautifulSoup(r.text, 'html.parser')

    try:
        categories = page_html.find_all('uc-breadcrumbs-link', {'itemprop': 'itemListElement'})
        category = ""
        for cat in categories[2:]:
            category += cat.text.strip() + ';'
        category = category[:-1]
    except:
        category = None

    return category


def parse_catalog(catalog: str, catalog_name: str, city: str):
    # Our link depends on city so we have to change it
    if city == "Москва":  # CHANGE THIS IF THERE WILL BE MORE THEN 2 CITIES
        catalog = catalog.replace("spb.","")
        prod_link = "https://leroymerlin.ru/"
    elif city == "СПб":
        prod_link = "https://spb.leroymerlin.ru/"

    page = 1
    checker = None
    flag = True
    products = []

    while(flag):
        # print('page: ',page)
        sapo_url = catalog +'?page='+str(page)
        # print(sapo_url)
        r = get(sapo_url, headers={'User-Agent': choice(useragents)}, proxies={'http': 'http://' + choice(proxies)})
        page_html = BeautifulSoup(r.text, 'html.parser')

        # sometimes page has these tags, but responses with 404 and it breaks the parser
        try:
            # get the list of containers with corresponding products in catalog page
            product_containers = page_html.find_all('div', class_="phytpj4_plp largeCard")
        except:
            continue

        if product_containers != []:
            for count, container in enumerate(product_containers):
                try:
                    link = prod_link + container.find('a')['href']  # link

                    if link == checker:
                        flag = False
                        break

                    if count == 0:
                        checker = link

                    title = container.find('a')['aria-label']  # title

                    article = container.find('span', class_='t3y6ha_plp sn92g85_plp p16wqyak_plp').text.replace("Арт. ", "")  # article

                    price_row = container.find('p', class_='t3y6ha_plp xc1n09g_plp p1q9hgmc_plp').text  # price
                    price = ""
                    for s in price_row:
                        if s.isdigit():
                            price += s

                    unit = container.find('p', class_='t3y6ha_plp x9a98_plp pb3lgg7_plp').text.split('/')[1][:-1]  # unit

                    category = parse_page(link)  # category

                    # We can't get these fields from this page
                    order = None  # order
                    inventory = None  # inventory
                    discount_price = None  # discount_price
                    stock = None  # stock
                    stock_name = None  # stock_name
                    price_2 = None  # price_2
                    discount_price_2 = None  # discount_price_2
                    unit_2 = None  # unit_2

                    # saving to csv
                    products.append([title,category,price,discount_price,link,"leroymerlin",catalog_name,stock,stock_name,article,unit,order,inventory,city,price_2,discount_price_2,unit_2])
                except:
                    print(link + '---')
                    pass

        page += 1
        sleep(randint(1,2))

    save_in_df(products)


def create_file():
    text_df = pd.DataFrame(columns =    ["title",
                                        "category",
                                        "price",
                                        "discount_price",
                                        "link",
                                        "site",
                                        "catalog",
                                        "stock",
                                        "stock_name",
                                        "article",
                                        "unit",
                                        "order",
                                        "inventory",
                                        "city",
                                        "price_2",
                                        "discount_price_2",
                                        "unit_2"])
    text_df.to_csv("lerua.csv", index=False)


def parse_ler_by_city(city):
    parse_catalog("https://spb.leroymerlin.ru/catalogue/pribory-ucheta-i-izmereniy/", "Приборы учета и измерений", city)


def csv2xlsx(filepath):
    read_file = pd.read_csv(filepath, encoding = "ISO-8859-1")
    read_file.to_excel(filepath.replace(".csv", "") + ".xlsx", index = None, header=True)


def parse_ler():
    create_file()
    parse_ler_by_city("Москва")
    parse_ler_by_city("СПб")
    csv2xlsx("lerua.csv")




parse_ler()
