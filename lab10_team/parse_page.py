from requests import get
from bs4 import BeautifulSoup
from random import choice

def parse_page(link):
    r = get(link, headers={'User-Agent': choice(useragents)})  # to get link with headers = User-Agents
    # print(link)
    page_html = BeautifulSoup(r.text, 'html.parser')

    # to not get an error when find_all didn`t find anything in parsing link
    try:
        categories = page_html.find_all('uc-breadcrumbs-link', {'itemprop': 'itemListElement'})
        category = ""  # merged row of categories
        for cat in categories[2:]:  # not only fist 2 rows
            category += cat.text.strip() + ';'
        category = category[:-1]
    except:
        category = None

    return category
