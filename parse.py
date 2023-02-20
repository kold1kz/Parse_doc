from bs4 import BeautifulSoup
from moves_table import *
import requests

mail = 'https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999#space-menu-link-content'

def forward_table(mail):
    page = requests.get(mail)

    soup = BeautifulSoup(page.text, 'html.parser')
    dict = []

    firststr = soup.find_all('th', class_='confluenceTh')
    allstr = soup.find_all('td', class_='confluenceTd')

    index = 0
    for data in firststr:
        dict.append(data.text)

    columns = len(dict)

    for data in  allstr:
        dict.append(data.text)

    rows = (len(dict))/columns


    create_table(rows,columns)

    for i in range(int(rows)):
        for j in range(columns):
            insert_txt(dict[index], i,j)
            index+=1


def update(mail):
    deleate_table()
    forward_table(mail)
    
