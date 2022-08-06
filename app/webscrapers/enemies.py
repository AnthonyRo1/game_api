from bs4 import BeautifulSoup
import requests


def get_all_enemies():
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Enemies')
    soup = BeautifulSoup(html_text.text, 'lxml')
    row_tags = soup.find_all('div', class_ = 'row')
    
    enemies_list = []
    for row in row_tags:
        h4_tags = row.find_all('h4')
        for header in h4_tags:
            if header.a:
                enemies_list.append({'tag': header, 'query': header.a['href'], 'name': header.text})

    return enemies_list
all_enemies = get_all_enemies()


def get_enemy_info(enemy_obj):
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com'
    html_text = requests.get(url + enemy_obj['query'])
    soup = BeautifulSoup(html_text.text, 'lxml')

    header_tags = soup.find_all('h3', class_ = 'bonfire')
    enemy_info = {
    }

    locations = []
    rewards = []
    for header in header_tags:
        if 'Location' in header.text or 'Locations' in header.text:
            ul = header.find_next_sibling()
            for li in ul:
                if li.text != '\n':
                    locations.append(li.text)
        if 'Rewards' in header.text:
            ul = header.find_next_sibling()
            for li in ul:
                if li.text != '\n':
                    rewards.append(li.text)

    enemy_info['name'] = enemy_obj['name']
    enemy_info['locations'] = locations
    enemy_info['rewards'] = rewards

    return enemy_info


enemy_info = get_enemy_info(all_enemies[0])