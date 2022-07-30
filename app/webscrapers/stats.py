from random import betavariate
from bs4 import BeautifulSoup
import requests




def get_all_stats(stat): 
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Stats')
    soup = BeautifulSoup(html_text.text, "lxml")
    tags = soup.find_all('h3', class_ = 'bonfire')
    all_stats = {

    }

    for tag in tags:
        print(tag.text)
        all_stats[tag.string] = []
    for tag in tags:
        if tag.text == stat:
            current_tag = tag
            while current_tag.find_next_sibling().name == 'p':
                current_tag = current_tag.find_next_sibling()
                print(current_tag.text)
            

       
    
get_all_stats('Posture')