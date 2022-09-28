from operator import length_hint
import requests
import numpy as np
from bs4 import BeautifulSoup

class Pokemon():
        def __init__(self, nome, tipo, total_status, hp, atk, defesa, sp_atk, sp_def, speed) -> None:
                self.nome = nome
                self.tipo = tipo
                self.total_status = total_status
                self.hp = hp
                self.atk = atk
                self.defesa = defesa
                self.sp_atk = sp_atk
                self.sp_def = sp_def
                self.speed = speed
        
        def print_status(self):
                print(self.nome,self.total_status)

#pagina que vamos trabalhar
url ='https://pokemondb.net/pokedex/all'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

lista = soup.find_all('option')
tipos = {}
cont = 0
for i in lista:
        tipos[i.get_text()] = cont
        cont+=1

indices = soup.find_all('span', class_='infocard-cell-data')
nomes = soup.find_all('a', class_='ent-name')
tipo = soup.find_all('td', class_='cell-icon')
total_status = soup.find_all('tr')
ind = []
for i in indices:
        ind.append(i.get_text())
#print(ind)
nome = []
for i in nomes:
        nome.append(i.get_text())
#print(nome)
ti = []
for i in tipo:
        linha = i.get_text().split()
        ti.append(linha)
#print(ti)
st = []
for status in total_status:
        aux = status.get_text().split()
        tam = len(aux)
        linha = []
        for i in range(tam-7,tam):
                linha.append(aux[i])
        st.append(linha)
#print(st)
ultimo = len(nome)
#print(len(ind),len(nome),len(ti),len(st))
with open ('pokedex.csv','a',newline='', encoding='utf-8') as f:
        for i in range(0, ultimo):
                linha = str(ind[i]) + ',' + str(nome[i]) + ',' + str(ti[i]) + ',' + str(st[i]) + ";\n"
                #print(type(ind[i]),type(nome),type(ti),type(st))
                #print(linha)
                f.write(linha)
print(ultimo)

