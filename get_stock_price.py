import requests_html
from bs4 import BeautifulSoup
from googlesearch import search


def stock_name(name):
    """the fun get stock name and return the URL in investing.com
    :param name: the stock name or symbol
    :type name: str
    :return: the URL of the stock in investing.com
    :rtype: str
    """
    query = f"{name} stock investing"
    for invest_url in search(query, tld="com", num=1, stop=1):
        return invest_url


def stock_number(invest_url):
    """the fun get URL and give information about the stock
    :param invest_url: the URL of the investing web
    :type invest_url: str
    :return: informaion about the stock
    :rtype: str
    """
    session = requests_html.HTMLSession()
    req = session.get(invest_url)
    bs = BeautifulSoup(req.text, "html.parser")
    try:
        stock_information = bs.find('div', {'class': 'top bold inlineblock'}).getText()
        stock_title = bs.find('h1', {'class':'float_lang_base_1 relativeAttr'}).getText()
        stock_currency = bs.find('div', {'class': 'bottom lighterGrayFont arial_11'}).getText().split()
        stock_list = stock_information.split()
        stock_price = stock_list[0]
        stock_change_price = stock_list[1]
        stock_percent = stock_list[2]

        if float(stock_percent[:-1]) > 0:
            price_str = f"""
            {stock_title}
            the stock price is: {stock_price} {stock_currency[-4]}
            the stock went up in: {stock_change_price} {stock_currency[-4]} 
            and it's worth: {stock_percent}
            """
            return price_str

        else:
            price_str2 = f"""
            {stock_title}
            the stock price is: {stock_price} {stock_currency[-4]}
            the stock get down in: {stock_change_price} {stock_currency[-4]} 
            and it's worth: {stock_percent}
            """
            return price_str2

    except AttributeError:
        error_str = "this stock does not exist"
        return error_str


if __name__ == '__main__':
    name = input("please give stock name or stock symbol:")
    stock_name(name)
    print(stock_number(stock_name(name)))

