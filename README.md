# Zillow Scraper

Zillow is an online property listing platform that millions of people use to search for homes. It is so popular there are even Super Bowl commercials joking about how people surf the website in their spare time. In addition to its popularity with the public, it is also a platform that is highly useful to real estate agents, brokers, developers, and investors. It has a searchable interface that allows the user to find details about home listings in a specific area. 


## What is This?
This is a web scraper that scrapes certain information from the Zillow website. If you need large amounts of home listings or infromation from Zillow or maybe you're just tired of scrolling through all the listings, then this web scraper can solve your problem. 

A web scraper is able to crawl a webpage, download the html, and then parse throught that html and scrape the information you want from the webpage. The advantages of web scrapers is that they collect large amounts of data very fast. If you need to prepare an excel workbook of home listings, this is the tool for you. 

Simply running this code will output an excel workbook containing 10 pages (400 properties) of listings for the city you choose.


# Usage

In order to use this program you should refernce the depencies and modules sections below. But right off the bat you will need Python (preferably Python 3). 

## Example
To run the program you will type "python3 Zillow_Scraper.py" into the terminal.

The program will run and it will prompt you for the name of a city:
```
Please enter a city name.
>
```

You can then respond by entering the name of a city by itself:
```
Dallas
```

Or you can be specific and enter the name of a city and state in the following format:
```
Dallas, -TX
```

This tells the program which city to scrape zillow data for. If you input Dallas, TX like above, then the program will scrape the first 10 pages of the Dallas, TX listings on Zillow.

Following that the code will prompt you for a location to save the output file to. You will need to give the path of the folder you want where you want to save the ouput of the program:
```
Enter location for this data to be saved:
>
```

You will need to enter a path name like:
```
/user/username/Desktop/projects/
```

Then the program will save the output of the program as an xlsm file with the name you gave for the city. 


The program will give you an excel file with seven (7) columns:

* prices
* address
* beds 
* last updated
* home type
* baths
* sqft



# Modules


# Dependencies


# Storing Data
