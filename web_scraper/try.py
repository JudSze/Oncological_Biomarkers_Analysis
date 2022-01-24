from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import regex as re
import wget
import pandas as pd
import pathlib 

global_list=[]
urls=[]
KEGG_links=[]
KEGG_list=[]

def get_KEGG_links(url):
    #links for each KEGG pathway site
    r=requests.get(url)
    soup=bs(r.text, 'html.parser')
    for link in soup.find_all('a'):
        l=link.get('href')
        urls.append(l)
    
    #links=soup.findAll('a', string=re.compile(x))
    mod_url='https://www.gsea-msigdb.org/gsea/'
    for link in urls:
        link=str(link)
        if 'KEGG' in link:
            KEGG_links.append(mod_url+link)
        else:
            continue
    
    for link in KEGG_links:
        r=requests.get(link, 'html.parser')
        soup=bs(r.text, 'html.parser')
        links=soup.findAll('a', string=re.compile("text"))
        mod_url='https://www.gsea-msigdb.org/gsea/'
        for link in links:
            KEGG_list.append(mod_url+link['href'])
            print(link)
        
        
        
    
    
get_KEGG_links('https://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp?collection=CP:KEGG')
len(KEGG_list)

for url in KEGG_list:
    text_url=url
    name=str(url).replace("https://www.gsea-msigdb.org/gsea/msigdb/download_geneset.jsp?geneSetName=","").replace("=txt",".txt")
    path="C:/Egyetem/Szakmai_gyak/KEGG_pathways/"+name
    wget.download(text_url, path)
    
#creating database out of all that information
root_dir = pathlib.Path('C:/Egyetem/Szakmai_gyak/KEGG_pathways/')
data = {}

for pth in root_dir.glob('*.txt'):
    data[pth.stem] = pd.read_table(pth)

df = pd.concat(data, axis=1)
df
df.to_csv('C:/Egyetem/Szakmai_gyak/KEGG_pathways/KEGG_df.csv')

