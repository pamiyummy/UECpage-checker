import requests
from bs4 import BeautifulSoup


def scraping() -> str:
    """url先のサイトの本文を取得して返す。

    Returns:
        str: サイトの本文（site-content-containというclassに属する文字列）
    """
    url = 'https://www.c1.uec.ac.jp/internal/b3/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all(class_='site-content-contain')[0].text
    return result
