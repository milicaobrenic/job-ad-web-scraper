#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:32:03 2022

@author: milica
"""

#from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

#driver = webdriver.Chrome("/home/milica/Downloads/chromedriver_linux64 (2)/chromedriver")

#driver.get("https://poslovi.infostud.com/oglasi-za-posao")

def posloviInfostud(max_pages):
    titles = []
    links = []
    companies = []
    cities = []
    deadlines = []
    descriptions = []
    
    for page_number in range (1, max_pages + 1):
        url = "https://poslovi.infostud.com/oglasi-za-posao?page={}".format(page_number)
        print('url:  ', url)
       # content = driver.page_source
       # soup = BeautifulSoup(content)
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "lxml")
        regex = re.compile('.*oglas_.*')
        for job in soup.findAll('div', attrs={'id': regex}):
       #     print('job: ', job)
            title = job.find('a', attrs={'data-product-type': 'link'})
            link = job.find('a', {'data-product-type':'link'}).get('href')
            print('link', link)
            company = job.find('p', attrs={'class':'uk-h4 uk-margin-remove'})
            city = job.find('p', attrs={'class':'uk-margin-remove-bottom'})
            deadline = job.find('p', attrs={'class':'uk-margin-remove uk-text-bold'})
            if job.find('p', attrs={'class':'job__desc'}) is not None:
                description = job.find('p', attrs={'class':'job__desc'})
            else:
                description = 'x'
                
            titles.append(title.text.strip())
            links.append(link)
            companies.append(company.text.strip())
            cities.append(city.text.strip())
            deadlines.append(deadline.text.strip())
            if(description != 'x'):
                descriptions.append(description.text.strip())   
            else:
                descriptions.append(description)
         
    df = pd.DataFrame()
    
    df['Title'] = titles
    df['Link'] = links
    df['Company'] = companies
    df['City'] = cities
    df['Deadline'] = deadlines
    df['Description'] = descriptions
    
    df.to_csv('jobsInfostud2.csv', index=False, encoding='utf-8')
    

def posloviLakodoposla(max_pages):
    titles = []
    links = []
    companies = []
    cities = []
    deadlines = []
    descriptions = []
    
    for page_number in range (1, max_pages + 1):
        url = "https://www.lakodoposla.com/index.php?mod=search&search=1&advanced=1&quick_search=1&start={}#jobs".format(page_number)
        #print('url: ', url)
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "lxml")
        for job in soup.findAll('div', attrs={'class':'NewJobs'}):
            print('job: ', job)
            title = job.find('a', attrs={'class': 'highlited_dark'})
            link = job.find('a', {'class':'highlited_dark'}).get('href')
            company = job.find('a', attrs={'class':'company_link'})
            city = job.find('span', attrs={'class':'lefty'})
            deadline = job.find('span', attrs={'class':''})
                    
            titles.append(title.text.strip())
            links.append(link)
            companies.append(company.text.strip())
            cities.append(city.text.strip())
            deadlines.append(deadline.text.strip())
            descriptions.append("x")    
         
        
    df = pd.DataFrame()
    
    df['Title'] = titles
    df['Link'] = links
    df['Company'] = companies
    df['City'] = cities
    df['Deadline'] = deadlines
    df['Description'] = descriptions
    
    df.to_csv('jobsLakodoposla2.csv', index=False, encoding='utf-8')

posloviInfostud(137)    
posloviLakodoposla(7)   
    
