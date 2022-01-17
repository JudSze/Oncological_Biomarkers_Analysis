from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import regex as re
import os
import urllib
import wget

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

print(global_list)

for url in global_list:
    text_url=url
    name=str(url).replace("https://www.gsea-msigdb.org/gsea/msigdb/download_geneset.jsp?geneSetName=","").replace("=txt",".txt")
    path="C:/Egyetem/Szakmai_gyak/KEGG_pathways/"+name
    wget.download(text_url, path)