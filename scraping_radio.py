from bs4 import BeautifulSoup #importing beautifulsoup
import requests
import re
import csv

page  = requests.get("https://radio.capital.pe/programas/viajeaotradimension")
soup= BeautifulSoup(page.content, 'html.parser')
box = soup.find(class_='box-mod') #finding the box where there are the information

'''You can filter multiple attributes at once by passing in more than one keyword argument:
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]'''
#table = box.findAll('a','item-listen play-button') #i just want the href informationand description
table = box.find_all(href=re.compile('#play'))


#getting dates and information
date = []
info = box.find_all('span','info')
for ifo in info:
    #print((ifo.get_text()))
    date.append(ifo.get_text())


#getting titles
titles = []
title = box.find_all('h2', 'title-podcast')
for ti in title:
    #print(ti.get_text())
    titles.append(ti.get_text())

#getting paragraph
para = []
description = box.find_all('div', 'description-podcast')
for des in description:
    #print(des.get_text())
    para.append(des.get_text())


#obteniendo links
links = []
for a in table:
    click = a.get('onclick') #getting onclick text
    if click != None: #dont do anything
        x= click.split("'media': '")  #splits the text with this coincidence 'media': '
        y = x[1].split("' , '") #splits the text with this coincidence ' , ' in order to obtain the url
        #print(y[0])
        links.append(y[0]) #adding urls to list


#creating a csv

rows = zip(titles,date,para, links)

with open('url_radio.csv', "w", newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in rows:
        writer.writerow(row)