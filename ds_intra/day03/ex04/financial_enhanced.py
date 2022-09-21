#!python3

import os
import sys
from bs4 import BeautifulSoup
from time import sleep
from urllib.request import urlopen, Request
import pstats

import ssl

def main():
    if len(sys.argv) != 3:
        raise Exception
    ticket = sys.argv[1]
    row_name = sys.argv[2]
    url = 'https://finance.yahoo.com/quote/{}/financials'.format(ticket)
    response = urlopen(Request(url=url, headers={'User-Agent': 'PYTHON'})).read()
    soup = BeautifulSoup(response, 'html.parser')


    mydivs = soup.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in mydivs]
    if row_name not in rows:
        raise Exception('Error with row')
    elems = mydivs[rows.index(row_name)].find_all('span')

    return tuple(elem.get_text() for elem in elems)


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        print(main())
    except Exception:
        print("error")


