#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests
from selenium import webdriver
import os


# In[2]:


# get_ipython().system('which chromedriver')


# In[3]:


executable_path = {'executable_path': '.\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA MARS NEWS

# In[4]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html= browser.html
soup= bs(html, 'html.parser')
news_title = soup.find("div", class_='content_title').get_text()
news_p = soup.find('div', class_='article_teaser_body').get_text()
print(news_title)
print(news_p)


# # JPL MARS SPACE IMAGES- FEATURED IMAGE

# In[5]:


url_image="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_image)
browser.click_link_by_partial_text('FULL IMAGE')
expand = browser.find_by_css('a.fancybox-expand')


# In[6]:


html_image = browser.html
soup = bs(html_image, 'html.parser')
featured_image_url= soup.find("img",{"class":"fancybox-image"})["src"]
mainurl="https://www.jpl.nasa.gov"
original_image_url= mainurl + featured_image_url
print(original_image_url)


# # Mars Facts

# In[7]:


web_url= "https://space-facts.com/mars/"
browser.visit(web_url)
html_web=browser.html
soup=bs(html_web, "html.parser")


# In[8]:


tab = pd.read_html(web_url)
# tab
mdf1=tab[0]
mdf2=tab[1]
mdf1.columns= ["Elements","Facts/Observations"]
mdf1.set_index("Elements", inplace= True)
html_table = mdf1.to_html()
# html_table


# In[9]:


html_table.replace('\n', '')


# # Mars Hemispheres

# In[10]:


browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
html = browser.html
soup = bs(html, 'html.parser')
hemis = []
results = soup.find_all('div', class_="collapsible results")
hemispheres = results[0].find_all('h3')

for x in hemispheres:
    hemis.append(x.text)
hemis


# In[11]:


thumbnail_results = results[0].find_all('a')
thumbnail_links = []

for thumbnail in thumbnail_results:
    if (thumbnail.img):
        thumbnail_url = 'https://astrogeology.usgs.gov/' + thumbnail['href']
        thumbnail_links.append(thumbnail_url)

thumbnail_links


# In[ ]:


image_list = []
for url in thumbnail_links:
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('img', class_='wide-image')
    image_path = results[0]['src']
    img_link = 'https://astrogeology.usgs.gov/' + image_path
    image_list.append(img_link)

image_list


# In[ ]:


hemisphere_zip = zip(hemis, image_list)
mars_urls = []

for title, i in hemisphere_zip:
    mars1 = {}
    mars1['title'] = title
    mars1['img_url'] = i
    mars_urls.append(mars1)

mars_urls


# In[ ]:


# !pip install nbconvert
# get_ipython().system('jupyter nbconvert --to python Mission_to_Mars.ipynb')

