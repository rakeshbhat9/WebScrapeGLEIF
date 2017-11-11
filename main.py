import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd
import time


def get_data():

    d = defaultdict(list)
    l = ['LEI', 'Legal Name', 'Other Entity Names', 'Transliterated Other Entity Names', 'Registration Authority ID',
         'Legal Jurisdiction', 'Entity Category', 'Entity Legal Form Code', 'Other Legal Form', 'Associated Entity',
         'Entity Status', 'Expiration Date', 'Expiration Reason', 'Successor Entity']

    url = 'https://www.gleif.org/lei/5493008JR8FCVQ6FJL94'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    for ul_tag in soup.find_all('ul', {'class': 'lei-LEIRecord'}):
        for li_tag in ul_tag.find_all('li'):
            for b in li_tag.find_all('b'):
                if b.text.encode('utf') in l:
                    try:
                        key = b.text.encode('utf')
                        if key == 'Entity Status':
                            value = li_tag.find('span').text.encode('utf').replace('\n', "").replace(" ", "")
                            d[key].append(value)
                        else:
                            value = li_tag.find('span').text.encode('utf').replace('\n', "")
                            d[key].append(value)

                    except:
                        key = b.text.encode('utf')
                        value = li_tag.find('div').text
                        d[key].append(value)
    data = pd.DataFrame(d)
    print data
    return data


if __name__ == '__main__':
    get_data()