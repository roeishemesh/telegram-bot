import requests_html
from bs4 import BeautifulSoup
from googlesearch import search


def crypto_name(name):
    """the fun get stock name and return the URL in investing.com
    :param name: the stock name or symbol
    :type name: str
    :return: the URL of the stock in investing.com
    :rtype: str
    """
    query = f"{name} value investing"
    for invest_url in search(query, tld="com", num=1, stop=1):
        return invest_url


def crypto_number(invest_url):
    """the fun get URL and give information about the stock
    :param invest_url: the URL of the investing web
    :type invest_url: str
    :return: information about the stock
    :rtype: str
    """
    session = requests_html.HTMLSession()
    req = session.get(invest_url)
    bs = BeautifulSoup(req.text, "html.parser")
    try:
        crypto_information = bs.find('div', {'class': 'top bold inlineblock'}).getText()
        crypto_title = bs.find('h1', {'class': 'float_lang_base_1 relativeAttr'}).getText()
        crypto_list = crypto_information.split()
        crypto_price = crypto_list[1]
        crypto_change_price = crypto_list[2]
        crypto_percent = crypto_list[3]
        if float(crypto_percent[:-1]) > 0:
            price_str = f"""
            {crypto_title}
            the crypto price is: {crypto_price} USD
            the crypto went up in: {crypto_change_price} USD
            and it's worth: {crypto_percent}
            """
            return price_str

        else:
            price_str2 = f"""
            {crypto_title}
            the crypto price is: {crypto_price} USD
            the crypto get down in: {crypto_change_price} USD
            and it's worth: {crypto_percent}
            """
            return price_str2

    except AttributeError:
        error_str = "this crypto does not exist"
        return error_str


if __name__ == '__main__':
    name = input("please give stock name or stock symbol:")
    crypto_name(name)
    print(crypto_number(crypto_name(name)))
