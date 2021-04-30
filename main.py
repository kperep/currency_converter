import requests
import argparse

url = 'https://api.exchangerate-api.com/v4/latest/USD'
currency = requests.get(url).json().get("rates")

global_amount = None
flag = False


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--from_currency', help='chose from currency', required=False, default=None)
    parser.add_argument('-t', '--to_currency', help='chose to currency', required=False, default=None)
    parser.add_argument('-a', '--amount', help='chose amount', required=False, default=None)
    return parser.parse_args()


def convert(from_currency, to_currency, amount):
    if from_currency != "USD":
        amount = amount / currency.get(from_currency)
    result = round(amount * currency.get(to_currency), 2)
    return result


def is_continue(result):
    cntn_with_amount = input('Continue with this result?: ')
    if cntn_with_amount == 'y':
        global global_amount
        global_amount = result
        global flag
        flag = True
        return True
    else:
        cntn_without_amount = input('Continue?: ')
        if cntn_without_amount == 'y':
            global_amount = None
            return True
        else:
            print('See you later!')
            return False


def get_data(argument_parser):
    if argument_parser.from_currency is None or flag:
        from_currency = input('Enter currency to convert: ')
    else:
        from_currency = argument_parser.from_currency
    if argument_parser.to_currency is None or flag:
        to_currency = input('What currency convert to?: ')
    else:
        to_currency = argument_parser.to_currency
    global global_amount
    if global_amount is None:
        if argument_parser.amount is None or flag:
            amount = float(input('Enter amount of currency: '))
        else:
            amount = float(argument_parser.amount)
    else:
        amount = global_amount
    return from_currency, to_currency, amount


def main():
    print('Welcome to my currency converter!')
    argument_parser = parse()
    while True:
        from_currency, to_currency, amount = get_data(argument_parser)
        result = convert(from_currency, to_currency, amount)
        print("Result: ", result)
        if is_continue(result):
            continue
        else:
            break


if __name__ == "__main__":
    main()
