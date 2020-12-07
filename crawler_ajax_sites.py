import requests
from time import sleep

# https://store.steampowered.com/search/?term=


def get_html(url):
    response = requests.get(url)
    if not response.ok:
        print(f'Code: {response.status_code}, url: {url}')
    return response.text


def main():
    start = 0
    url = f'https://store.steampowered.com/search/results/?query&start={start}&count=100&infinite=1'
    while True:
        print(url)
        if True:
            start += 100
            url = f'https://store.steampowered.com/search/results/?query&start={start}&count=100&infinite=1'
        else:
            break


if __name__ == '__main__':
    main()
