# Eslite (誠品) Online Bookstore Web Scraper Using Selenium
                                                                                                               
Eslite Bookstore is one of the largest Book/ Stationery Store in Taiwan. This web scraper allows you to search for a specific keyword and will automatically fetch the **product names** and **prices** from the Eslite Online Bookstore (www.eslite.com) and store the data in a Pandas DataFrame for further analysis.

Here is how this web scraper works:

* A Python Script that does following:
  1. Initialize the Chrome Driver
  2. Search the URL (www.eslite.com)
  3. Locate the HTML elements like search bar/no of results/product names/prices etc. via tag/name/XPath
  4. Parse the selected HTML elements and store them in a DataFrame
  5. Include action chains that perform the automation like redirecting to the next page

* Execute the script via the Chrome *Driver* to perform tasks on the Chrome *Browser*

## How to use it

1. Install Chrome *Browser* and Chrome *Driver* (Note: They are different)

Why -> The Chrome Driver acts as a bridge for the Python script to perform tasks on the Chrome Browser

Chrome Browser: https://www.google.com/intl/en_ca/chrome/

Chrome Driver: https://googlechromelabs.github.io/chrome-for-testing/ 

Make sure the driver has the same version as the browser!!
<br/><br/>

2. Install Selenium, Pandas and tqdm in the terminal

Why -> Selenium is the framework I am using to parse the HTML and perform automation, Pandas for storing the data and tqdm for visualizing the fetching progress


```
pip install selenium
pip install pandas
pip install tqdm
```


3. Documentation

As for now (Version 1.0), there is only one function for this web scraper.

1. Use **.scrape()** to perform scraping

```
EsliteScraper().scrape("keyword here", no_of_pages)
```
The argument **no_of_pages** indicates the pages you want to fetch for (20 products per page), you can also choose to leave it blank and it will fetch all the results.

## Problems 
The code might encounter errors like **StaleElementError**, **ValueError**, etc. This is
 because the program starts to locate the HTML elements before the website has fully reloaded.
Please consider run the program again or limit the number of pages to fetch. 
I am currently working on this issue and it will be fixed in the upcoming version. Thank you for your understanding!