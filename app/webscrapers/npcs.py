from bs4 import BeautifulSoup
import requests

def get_all_npcs():
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/NPCs+and+Characters')
    soup = BeautifulSoup(html_text.text, 'lxml')
    tags = soup.find_all('h3', class_ = 'special')

    all_npcs = [];
    for tag in tags:
        all_npcs.append(tag.string)
    return all_npcs

npc_list = get_all_npcs()






def npc_description(npc):
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com/'
    query = ''
    if len(npc.split(" ")) > 1:
        query = "+".join(npc.split(" ")) 
    else:
        query = npc

    html_text = requests.get(url + query)
    soup = BeautifulSoup(html_text.text, 'lxml')
    
    description = []
    location = []
    title_tags = soup.find_all('h3', class_ = 'bonfire')
    tbody = soup.find('tbody')


    for tag in title_tags:
        if 'Information' in tag.text:
            current_tag = tag.find_next_sibling()
            while current_tag.name == 'p':
                description.append(current_tag.text)
                current_tag = current_tag.find_next_sibling()


            while current_tag.name == 'ul':
                all_li = current_tag.find_all('li')
                for li in all_li:
                    if 'Location' in li.text:
                        location.append(li.text)
                    else:
                        description.append(li.text)
                current_tag = current_tag.find_next_sibling()
            
            

    quests = ''
    for tag in title_tags:
        if 'Quests' in tag.text:
            current_tag = tag.find_next_sibling()
            while current_tag.name == 'ul':
                quests += current_tag.text
                current_tag = current_tag.find_next_sibling()

    td_tags = tbody.find_all('td')
    if npc != 'Sekiro':
        for td in td_tags:
            if td.string == 'Location':
                td_next = td.find_next_sibling()
                td_next_a = td_next.find_all('a')
                if len(td_next_a) > 0:
                    for a in td_next_a:
                        location.append(a.text)
                else:
                    location.append(td_next.text)



    if len(description) > 1:
        description = '\n\n'.join(description)
    else:
        description = description[0]
    
    if npc != "Sekiro":
        return {
            'description': description,
            'quests': quests,
            'location': location
        }
    else: 
        return {
            'description': description,
            'quests': quests,
        }

npc_description('Sekiro') # Kuro The Divine Heir 