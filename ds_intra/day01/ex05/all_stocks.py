import sys


def all_stocks(argv):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    rev_companies = {v: k for k, v in companies.items()}

    arr = argv.replace(' ', '').split(',')
    if '' in arr:
        return
    for i in arr:
        up = i.upper()
        cap = i.capitalize()
        if up in stocks:
            print("{} is a ticker symbol for {}".format(up, rev_companies[up]))
        elif cap in companies:
            print("{} stock price is {}".format(cap, stocks[companies[cap]]))
        else:
            print("{} is an unknown company or an unknown ticker symbol".format(i))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        all_stocks(sys.argv[1])
