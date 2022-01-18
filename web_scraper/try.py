from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import regex as re
import wget
import pandas as pd
from pathlib import Path

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
    
    
get_KEGG_links('https://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp?collection=CP:KEGG', 'TRANSPORTERS')
print(global_list)

for url in global_list:
    text_url=url
    name=str(url).replace("https://www.gsea-msigdb.org/gsea/msigdb/download_geneset.jsp?geneSetName=","").replace("=txt",".txt")
    path="C:/Egyetem/Szakmai_gyak/KEGG_pathways/"+name
    wget.download(text_url, path)
    
len(global_list)

#creating database out of all that information
root_dir = pathlib.Path('C:/Egyetem/Szakmai_gyak/KEGG_pathways/')
data = {}

for pth in root_dir.glob('*.txt'):
    data[pth.stem] = pd.read_table(pth)

df = pd.concat(data, axis=1)
df
df.to_csv('C:/Egyetem/Szakmai_gyak/KEGG_pathways/KEGG_df.csv')

