from random import betavariate
from bs4 import BeautifulSoup
import requests

def get_all_npcs():
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/NPCs+and+Characters')
    soup = BeautifulSoup(html_text.text, 'lxml')
    tags = soup.find_all('h3', class_ = 'special')

    all_npcs = [];
    for tag in tags:
        all_npcs.append(tag.string)