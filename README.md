# Booking.com Hotel Data Scraper

## Overview
This Python script automates the extraction of hotel data from Booking.com for Belgrade. It's designed to gather details like hotel names, locations, ratings, price information, and other relevant data, and then export this information to Excel and CSV formats for further analysis.

## Requirements
Python 3.8 or higher
Libraries: requests, BeautifulSoup4, pandas, matplotlib, numpy, fake_useragent

## Setup
To run this script, you must install the required Python libraries. You can install these using pip:

pip install beautifulsoup4 requests pandas matplotlib numpy fake_useragent


## Usage
To execute the script, navigate to the script's directory and run:

scraping_bookingcom_belgrad.ipynb

Ensure you have an internet connection as the script needs to access Booking.com to retrieve data.

## Data Collection
The script collects the following details for each hotel listing on Booking.com for the specified date range:

Hotel Title
Location
Rating
Rating Category
Number of Reviews
Price for Two Adults
Taxes and Other Charges
Booking Link
Data Export

After scraping the data, the script saves it in two formats:

An Excel file named bookingcom_belgrad.xlsx
A compressed CSV file within a ZIP named bookingcom_belgrad.zip
These files are stored in the same directory as the script.

## Customization
You can modify the script to scrape data for different dates or other locations by changing the url_list variable. Ensure to adjust the date and location parameters within the URLs.

## Disclaimer
This script is for educational purposes only. Frequent requests to Booking.com might lead to your IP being temporarily blocked, so use responsibly and consider the website's terms of service.
