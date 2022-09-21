#!python3
from time import sleep
import requests, sys, pytest
from bs4 import BeautifulSoup


def test_parse_ticker():
    res = parse('MSFT', 'Total Revenue')
    assert res[0] == 'Total Revenue'


def test_parse_tuple():
    res = parse('MSFT', 'Total Revenue')
    assert type(res) == tuple


def test_parse_url():
    try:
        parse('MSweFT', 'Total Revenue')
        assert False
    except Exception:
        assert True


def main():
    """
    Main function.
    """
    if len(sys.argv) != 3:
        raise Exception
    ticket = sys.argv[1]
    row_name = sys.argv[2]
    res = parse(ticket, row_name)
    if res:
        print(res)


def parse(ticket, row_name):
    url = "https://finance.yahoo.com/quote/{}/financials".format(ticket)
    try:
        response = requests.get(url, headers={'User-Agent': 'PYTHON'})
    except requests.exceptions.ConnectionError as e:
        print("error")
    soup = BeautifulSoup(response.text, 'html.parser')

    mydivs = soup.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in mydivs]
    if row_name not in rows:
        raise Exception('Error with row')
    elems = mydivs[rows.index(row_name)].find_all('span')

    return tuple(elem.get_text() for elem in elems)


if __name__ == '__main__':
    try:
        print(main())
    except Exception:
        print("error")

# pytest
