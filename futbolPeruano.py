

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

# pts = 2
# dg  = 4
# gc  = 6
# gf  = 8
# p   = 10
# E   = 12
# g   = 14
# pj  = 16

# URL del sitio web a hacer scraping
url = 'https://www.futbolperuano.com/liga-2/tabla-de-posiciones'

html = urlopen( url )
bs = BeautifulSoup(html.read(), 'html.parser')

def extraer_numeros(cadena):
    numero = re.search(r'[+-]?\d+', cadena)
    if numero:
        numero = int(numero.group())
    return numero

def getImgTeams():
    try:
        listImg = []
        ImgTeams = bs.find('table', {'class':'table'}).find_all_next('td',{'class':'equipo'})
        for item in ImgTeams:
            listImg.append(item.img.attrs['data-src'])
    except TabError as e:
        print('ERROR GET IMG TEAMS')
        return None
    return listImg

def getNameTeams():
    try:
        listName = []
        nameTeams = bs.find_all('span',{'class':'d-md-inline'})
        for name in nameTeams:
            listName.append(name.get_text())
    except TabError as e:
        print('ERROR GET NAMES TEAMS')
    return listName

def getDataTeams(pos = 2):
    try:
        allDataTemas = bs.find('table', {'class':'table'}).find_all_next('tr')
        listdata = []
        for id, data in enumerate(allDataTemas):
            if( id != 0):
                item = str(data).split(sep='td');
                listdata.append( extraer_numeros(str(item[len(item)-pos])) )
    except TabError as e:
        print('ERROR GET IMG TEAMS')
        return None
    return listdata

def getAllTablePositions():
    
    try:
        listaNames = getNameTeams()
        listaImgTeams = getImgTeams()
        listaPj = getDataTeams(16)
        listaG = getDataTeams(14)
        listaE = getDataTeams(12)
        listaP = getDataTeams(10)
        listaGf = getDataTeams(8)
        listaGc = getDataTeams(6)
        listaDG = getDataTeams(4)
        listaPts = getDataTeams(2)
        teams = []
        for name, imgTeam, pg, g, e, p, gf, gc, dg, pts in zip(listaNames, listaImgTeams, listaPj, listaG, listaE, listaP, listaGf, listaGc, listaDG, listaPts):
            resDG = ('+' + str(dg)) if dg > 0 else ('-' + str(abs(dg)))
            teams.append({
                'name':name,
                'img': imgTeam,
                'PG':pg,
                'G':g,
                'E':e,
                'P':p,
                'GF':gf,
                'GC':gc,
                'DG':resDG,
                'PTS':pts
            })
    except TabError as e:
        return None
    return teams
    
    

getImgTeams()