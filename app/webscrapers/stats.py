from bs4 import BeautifulSoup
import requests

def get_all_stats():
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Stats')

    soup = BeautifulSoup(html_text.text, "lxml")
    tags = soup.find_all('h3', class_ = 'bonfire')
    all_stats = []
    for tag in tags:
        all_stats.append(tag.text)
    return all_stats

all_stats = get_all_stats()




# This function takes in a 'stat' as an argument, parses the page for all h3 tags containing the given 'stat', and then finds all of the sibling p tags' text content-- which results in the description of said 'stat'
def get_stat_descriptions(stat): 
    html_text = requests.get('https://sekiroshadowsdietwice.wiki.fextralife.com/Stats')
    soup = BeautifulSoup(html_text.text, "lxml")
    tags = soup.find_all('h3', class_ = 'bonfire')
    description = ''
    for tag in tags:
        if tag.text == stat:
            current_tag = tag
            while current_tag.find_next_sibling().name == 'p':
                current_tag = current_tag.find_next_sibling()
                description += current_tag.text
    
    return description




# returns "Stat name": { "description": "stat-description"}
def stats_obj():
    stats_and_desc = []
    for stat in all_stats:
        stats_and_desc.append(
            {
                stat: {'description': get_stat_descriptions(stat)}
            }
            )
    return stats_and_desc

# returns List of stat names in the same order as stats_obj()
def stat_names_list():
    return all_stats

