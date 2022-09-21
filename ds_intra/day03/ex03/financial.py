#!python3
import os
import sys
import requests
from bs4 import BeautifulSoup
from time import sleep


def main():
    sleep(5)
    if len(sys.argv) != 3:
        raise Exception
    ticket = sys.argv[1]
    row_name = sys.argv[2]
    url = "https://finance.yahoo.com/quote/{}/financials".format(ticket)
    response = requests.get(url, headers={'User-Agent': 'PYTHON'})
    # if response != 200: //<class 'requests.models.Response'>
    #     raise Exception
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
