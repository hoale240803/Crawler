import requests
from time import sleep  # library of python to sleep
from bs4 import BeautifulSoup
import re  # library of python to write Regular expressions
# https://store.steampowered.com/search/?term=
import csv  # library of python to export .csv file


def write_csv(data):
    with open('result.csv', 'a', encoding="utf-8") as f:
        fields = ['title', 'reviews', 'released', 'tags']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(data)


def get_html(url):
    response = requests.get(url)
    if not response.ok:
        print(f'Code: {response.status_code}, url: {url}')
    return response.text


def get_games(html):
    soup = BeautifulSoup(html, 'lxml')
    pattern = r'^https://store.steampowered.com/app/'  # r character meaning raw string
    games = soup.find_all('a', href=re.compile(pattern))
    return games


def get_hover_data(id):
    # f character meaning that string had expression
    url = f'https://store.steampowered.com/apphoverpublic/{id}'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        # strip is function of python to trim string
        # strip meaning trimp()
        title = soup.find('h4', class_='hover_title').text.strip()
    except:
        title = ''
        print(url)

    try:
        # to get data as "Released : 17 Dec, 2019"
        released = soup.find(
            'div', class_='hover_release').text.split(':')[-1].strip()  # tupple view more https://www.w3schools.com/python/python_tuples_access.asp
    except:
        released = ''
        print(url)

    try:
        # to get data as " Very Positive (1,835)"
        reviews_raw = soup.find(
            'div', class_='hover_review_summary').text.strip()
    except:
        reviews = ''
        print(url)
    else:
        pattern = r'\d+'
        # tìm tất cả là số trong string
        reviews = int(''.join(re.findall(pattern, reviews_raw)))

    try:
        # to get data as "User tags: xxx \n xxx \n xxx"
        tags_raw = soup.find_all('div', class_='app_tag')
    except:
        tags = ''
        print(url)
    else:
        # list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
        tags_text = [tag.text for tag in tags_raw]
        tags = ', '.join(tags_text)
    data = {
        'title': title,
        'released': released,
        'reviews': reviews,
        'tags': tags
    }
    write_csv(data)


def main():
    all_games = []
    start = 0
    # note  example "infinite=1" this param mean that only one request
    url1 = f'https://store.steampowered.com/search/results/?query&start={start}&count=100&tags=3859%2C19%2C492%2C4182'
    # url = f'https://store.steampowered.com/search/results/?query&start={start}&count=100'
    while True:
        games = get_games(get_html(url1))
        print(url1)
        if games:
            all_games.extend(games)
            start += 100
            url1 = f'https://store.steampowered.com/search/results/?query&start={start}&count=100&tags=3859%2C19%2C492%2C4182'
            # url = f'https://store.steampowered.com/search/results/?query&start={start}&count=100'

        else:
            break
    print(len(all_games))
    for game in all_games:
        id = game.get('data-ds-appid')
        get_hover_data(id)


if __name__ == '__main__':
    main()
