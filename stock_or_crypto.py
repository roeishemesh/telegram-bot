import crypto_value as cry
import get_stock_price as get

def stock_or_crypto(name):
    if "crypto" in name:
        return cry.crypto_number(cry.crypto_name(name))
    else:
        return get.stock_number(get.stock_name(name))


if __name__ == '__main__':
    dog = input("what you want to search:")
    print(stock_or_crypto(dog))