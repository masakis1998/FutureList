from lxml import html
import requests
import re
import json


def get_data(id_ref):

    page = requests.get('https://api.jikan.moe/anime/{}'.format(id_ref))
    tree = html.fromstring(page.content)

    text = tree.xpath('text()')[0]
    index = re.search(',"opening_theme"', text)

    if (index):
        index = index.span()[0]

        text = text[:index] + '}'

    text = json.loads(text)

    return text


def get_stats(id_ref):

    page = requests.get('https://api.jikan.moe/v3/anime/{}/stats'.format(id_ref))
    tree = html.fromstring(page.content)

    text = tree.xpath('text()')[0]

    text = json.loads(text)

    return text

def get_staff(id_ref):

    page = requests.get('https://api.jikan.moe/v3/anime/{}/characters_staff'.format(id_ref))
    tree = html.fromstring(page.content)

    text = tree.xpath('text()')[0]

    text = json.loads(text)

    text = text['staff']
    return text
