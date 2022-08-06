from bs4 import BeautifulSoup
import requests

def get_all_bosses():
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com/Bosses'
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')

    boss_elems = soup.find('div', class_ = 'tabcontent 1-tab tabcurrent')
    
    h4_tags = boss_elems.find_all('h4', class_ = 'special')
    
    all_bosses = []
    for tag in h4_tags:
        all_bosses.append({'query': tag.a['href'], 'name': tag.text})
    return all_bosses


all_bosses = get_all_bosses()
print(len(all_bosses))



def get_boss_info(boss_obj):
    query = boss_obj['query']
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com'
    html_text = requests.get(url + query)
    soup = BeautifulSoup(html_text.text, 'lxml')



get_boss_info(all_bosses[0])