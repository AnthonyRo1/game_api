from bs4 import BeautifulSoup
import requests




def get_prosthetic_tools(): 
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Prosthetic+Tools')
    soup = BeautifulSoup(html_text.text, "lxml")

    shinobi_prosthetics = []
    tags = soup.find_all('h3', class_ = 'special')
    for tag in tags:
        shinobi_prosthetics.append(tag.a.string)
    
    return shinobi_prosthetics


def get_all_prosthetic_upgrades():
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Prosthetic+Tool+Upgrades')
    soup = BeautifulSoup(html_text.text, 'lxml')
    
    tags = soup.find_all('h3', class_ = 'special')
    all_upgrades = []
    for tag in tags: 
        print(tag.text)
        all_ps = tag.find_next_siblings('p')
        for p in all_ps:
            all_as = p.a
            if (all_as is not None):
                all_upgrades.append([a.string for a in all_as if a is not None][1])
    return all_upgrades


def get_single_prosthetic_upgrades(prosthetic_tool):
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Prosthetic+Tool+Upgrades')
    soup = BeautifulSoup(html_text.text, 'lxml')
    tags = soup.find_all('h3', class_ = 'special')

    all_upgrades = []
    for tag in tags:
        if tag.string == prosthetic_tool:
            p_tags = tag.find_next_siblings()
            for p in p_tags:
                if p.text != '\xa0':
                    all_upgrades.append(p.text)

    return all_upgrades
 # function to be invoked with prosthetic tool, the prosthetic tool should be case-whitespace-sensitive 




# 1. NOTE Returns an array in the form of [ [how to use], [location] ]
def get_tool_info(prosthetic_tool):
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com'
    if len(prosthetic_tool.split(" ")) > 1:
        words = prosthetic_tool.split(" ")
        query = "+".join([word.capitalize() for word in words])
        url += f'/{query}'
        
    
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    tag = soup.find('div', class_ = 'infobox')
    description = tag.find_next_sibling().text
    block = soup.find('tbody').find('img')
    info_block_title = soup.find_all('h3')
    

    ## NOTE HOW TO USE
    how_to_use = []
    for tag in info_block_title:
        if 'How to use' in tag.string:
            for li in list(tag.find_next_sibling().children):
                if list(li.strings)[0] != '\n':
                    how_to_use.append(li.text)
    if len(how_to_use) > 1:
        how_to_use = "\n\n".join(how_to_use)
    elif len(how_to_use) == 1:
        how_to_use = how_to_use[0]

    ## NOTE WHERE TO FIND 
    location = []
    for tag in info_block_title:
        if 'Where to find' in tag.string:
            for li in list(tag.find_next_sibling().children):
                if list(li.strings)[0] != '\n':
                    location.append(li.text)

    return {
        'description': description,
        'use': how_to_use,
        'location': location,
        'upgrades': get_single_prosthetic_upgrades(prosthetic_tool)
    }




def get_upgrade_info(prosthetic_upgrade):
    url = 'https://sekiroshadowsdietwice.wiki.fextralife.com/'
    query = ''
    if len(prosthetic_upgrade.split(" ")) > 1:
        query = "+".join(prosthetic_upgrade.split(" "))
    else:
        query = prosthetic_upgrade
    
    html_text = requests.get(url + query)
    soup = BeautifulSoup(html_text.text, 'lxml')
    title_tag = soup.find('div', id='infobox')


    current_p = title_tag.find_next_sibling()
    description = []
    while current_p.name == 'p':
        description.append(current_p.text)
        current_p = current_p.find_next_sibling()

    print("\n\n".join(description))

    return {
        'description': description
    }

get_upgrade_info('Lazulite Axe')