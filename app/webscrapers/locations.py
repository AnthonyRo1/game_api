from bs4 import BeautifulSoup
import requests


def get_all_locations():
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Locations')
    soup = BeautifulSoup(html_text.text, 'lxml')
    tags = soup.find_all('h3', class_ = 'special')

    all_locations = [];
    for tag in tags:
        all_locations.append(tag.string)
    return all_locations

location_list = get_all_locations()


def get_location_info(location):
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com/'
    query = ''
    if len(location.split(" ")) > 1:
        query = "+".join(location.split(" "))
    else:
        query = location

    html_text = requests.get(url + query)
    soup = BeautifulSoup(html_text.text, 'lxml')
    description = soup.find('div', id='wiki-content-block').find('p')
    
    title_tags = soup.find_all('h3', class_ = 'special')

    bosses = []
    for tag in title_tags: 
        if 'Bosses' in tag.text:
            title_tag_next = tag.find_next_sibling()
            if title_tag_next.name == 'ul':
                title_tag_li = title_tag_next.find_all('li')
                for li in title_tag_li:
                    bosses.append(li.text)
    items = []
    for tag in title_tags: 
        if 'Items' in tag.text:
            current_next = tag.find_next_sibling()
            while current_next.name != 'h3':
                if current_next.name == 'p':
                    next_ul = current_next.find_next_sibling()
                    if next_ul.name == 'ul':
                         [items.append(each_li.text) for each_li in next_ul.find_all('li')]
                current_next = current_next.find_next_sibling()
    enemies = []
    for tag in title_tags:
        if 'Enemies' in tag.text:
            next_ul = tag.find_next_sibling()
            if next_ul.name == 'ul':
                each_li = next_ul.find_all('li')
                [enemies.append(li.text) for li in each_li]
    npcs = []
    for tag in title_tags:
        if 'NPCs in the area' in tag.text:
            next_ul = tag.find_next_sibling()
            if next_ul.name == 'ul':
                each_li = next_ul.find_all('li')
                [npcs.append(li.text) for li in each_li]
    
    return {
        'location': location,
        'description': description,
        'NPCs': npcs,
        'bosses': bosses,
        'items': items,
        'enemies': enemies
    }
