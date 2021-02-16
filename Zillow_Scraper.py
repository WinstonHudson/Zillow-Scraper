import os
from selenium import webdriver
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import lxml
import numbers
from bs4 import BeautifulSoup
import requests



# Headers are a way to access the page from our scraper (instead of the previous website page)
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

base_url = "https://www.zillow.com/homes/for_sale/"



#get urls
def get_urls():
    urls = []
    pages = ['2','3','4','5','6','7','8','9','10']

    # Gather the urls of the zillow pages we will call and store them in dictionary
    print('Please enter a city name.')
    city = input()
    url1 = base_url +city+'/'
    urls.append(url1)
    for i in pages:
        dom = base_url + city +'/'+i+'_p/'
        urls.append(dom)
        
    return urls, city;


# Extract data from urls w/BeautifulSoup
def soups(url):
    with requests.Session() as s:
        
        r = s.get(url, headers=req_headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        
    return soup


# Parse data and store in dictionary
def parse_soup(urls):

    dic = []

    for url in urls:
        my_url = soups(url)
        dic.append(my_url)
        
    return dic


# Call this funciton for crawler to scrape values we want 
def my_scraper(data):

    df = pd.DataFrame()

    #for i in data:
    address = data.find_all (class_= 'list-card-addr')
    price = list(data.find_all (class_='list-card-price'))
    beds = list(data.find_all("ul", class_="list-card-details"))
    last_updated = data.find_all ('div', {'class': 'list-card-top'})
    
    df['prices'] = price
    df['address'] = address
    df['beds'] = beds
    df['last_updated'] = last_updated
    
    # We use copy so that we can store the df's in different variables
    # otherwise all the variables will change everytime we change the global df
    return df.copy()


# Cycle through each html extract in our dictionary and store output in new dataframe
def zillow_table(html_soup):

    zillow_df = pd.DataFrame()

    df_list = []
    
    #use my_soup() function
    for soup in html_soup:
        new_df = my_scraper(soup)
        df_list.append(new_df)

    # Combine df's in our list
    zillow_df = pd.concat(df_list)
    zillow_df.reset_index(inplace=True)
    zillow_df = zillow_df.drop('index', axis=1)

    return zillow_df


# Clean the data in the dataframe
def clean_data(dataframe):
    
    df = dataframe.applymap(str)
    new_df = df.applymap(lambda x: re.sub('<[^<]+?>', '',x))

    # separate beds column into bed, bath, and sq_feet
    new_df[['beds', 'home_type']] = new_df.beds.str.split('-',n=1, expand=True)
    new_df[['beds', 'baths', 'sqft']] = new_df.beds.str.split(',',n=2, expand=True)
    
    return new_df


def conv_csv(dataframe, city):


    print("Enter location for this data to be saved:")
    path_to_output = input()
    
    zillow_listing_data = dataframe.to_excel(path_to_output + city+"_zillow_listings.xlsx", sheet_name='sheet1', index=False)

    return zillow_listing_data


def main():
    
    # get the input from the user and gather urls
    urls, city = get_urls()

    #html_soup function runs the soup function inside of it
    html_soup = parse_soup(urls)

    # Calls the web scraper and makes a dataframe of the scraped values
    zillow_df = zillow_table(html_soup)

    #Clean the data and make new features
    final_df = clean_data(zillow_df)

    # Convert to csv
    zillow_csv =  conv_csv(final_df, city)
    

    return zillow_csv


    
main()
    
    
