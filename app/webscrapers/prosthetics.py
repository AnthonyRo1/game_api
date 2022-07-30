from random import betavariate
from bs4 import BeautifulSoup
import requests




def get_shinobi_tools(): 
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
            all_ps = tag.find_next_siblings('p')
            for p in all_ps:
                all_as = p.a
                if (all_as is not None):
                    all_upgrades.append([a.string for a in all_as if a is not None][1])

    return all_upgrades
 # function to be invoked with prosthetic tool, the prosthetic tool should be case-whitespace-sensitive 

