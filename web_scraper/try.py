from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import regex as re

#definiálj egy listát és itt legyen üres
global_list=[]

def get_KEGG_links(url, x):
    #links for each KEGG pathway site
    r=requests.get(url, 'html.parser')
    soup=bs(r.text, 'html.parser')
    links=soup.findAll('a', string=re.compile(x))
    mod_url='https://www.gsea-msigdb.org/gsea/'
    KEGG_links=[mod_url+link['href'] for link in links]
    
    #links for gene set text file
    for link in KEGG_links:
        if link.endswith('txt'):
            print(link)
            global_list.append(link)
        get_KEGG_links(link, 'text')
    
    
get_KEGG_links('https://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp?collection=CP:KEGG', 'KEGG')
#iratsd ki a listát

print(global_list)