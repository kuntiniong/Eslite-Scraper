from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
import pandas as pd 
import time

class EsliteScraper:
    # public:
    def scrape(self, search_term, no_of_pages = None):

        # approach:
        # open browser-> search url -> search products -> get the no of pages -> 
        # (parse HTML -> next page)* no of pages -> store in a pandas DataFrame
        URL = "https://www.eslite.com/"

        self._initializeDriver()
        self.driver.get(URL) 
        time.sleep(1) 
        self._searchProducts(search_term)
        time.sleep(1.5)

        self.no_of_pages = self._getPageNumber() if no_of_pages is None else no_of_pages # constructor
        df = pd.DataFrame()
        for i in tqdm(range(self.no_of_pages)):
            df = pd.concat([df, self._fetchData()], axis = 0, ignore_index = True)
            if i < self.no_of_pages-1:
                self._nextPage()
        self.driver.quit()
        return df

    # private:
    def _initializeDriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--blink-settings=imagesEnabled=false') # disable the images to speed up 
        self.driver = webdriver.Chrome(options = chrome_options) 

    def _searchProducts(self, search_term):
        search = self.driver.find_element(By.TAG_NAME, "input") # locate the search bar
        search.send_keys(search_term)
        search.send_keys(Keys.RETURN)

    def _getPageNumber(self):
        no_of_results = int(self.driver.find_element(By.XPATH, 
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[3]').text)
        no_of_pages = int(no_of_results/20) if no_of_results%20 == 0 else int(no_of_results/20)+1 # 20 results per page
        return no_of_pages

    def _fetchData(self): # per page
        def objectToText(object_list, col_name): # .find_elements() method returns a list of objects
            return pd.DataFrame(data = [x.text for x in object_list], columns = [col_name])
        
        product_name_list = objectToText(self.driver.find_elements(By.CLASS_NAME, "product-name"), "Product Name")
        price_list = objectToText(self.driver.find_elements(By.CLASS_NAME, "price"), "Price")

        print(len(price_list))

        data_df = pd.concat([product_name_list, price_list], axis = 1)
        data_df["Price"] = data_df["Price"].str.replace(",", "").astype(int) # remove "," and typecast the string(price) to integer
        return data_df

    def _nextPage(self):
        # press "end"  -> press "next page" 
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END)
        actions.perform()
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, 
        '//a[@data-v-ae739145 and @href="javascript:void(0);"]/span[@data-v-ae739145 and contains(@class, "icon-fa-chevron-right")]'))
        time.sleep(2)