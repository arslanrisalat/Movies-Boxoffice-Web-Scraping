from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time
from datetime import date

class movie:
    def __init__(self):
        self.path = os.getcwd()
        #print(self.path)
        self.driver = webdriver.Chrome()
        self.BASEURL = "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"

        self.extract_data()
        self.load_csv()
        self.driver.close()
   
    def extract_data(self):
        self.driver.get(self.BASEURL)
        movies_section = self.driver.find_elements(By.XPATH,'//td[@class="a-text-left mojo-field-type-title"]/a[@class="a-link-normal"]')  ## targets all the elements on the web that has same Xpath
        self.movie_name = []                                                                                              ## an empty list for storing movie names
        for movie in range(len(movies_section)):                                                                                      ## a loop that runs until the length of movies_name list
            self.movie_name.append(movies_section[movie].text)                                                                        ## extracting text from the movie name and appending it on the movies name list
        #print(movie_name)

        gross_section = self.driver.find_elements(By.XPATH,'//td[@class="a-text-right mojo-field-type-money"]') 
        self.lifetime_gross = []
        for i in range(len(gross_section)):
            self.lifetime_gross.append(gross_section[i].text)
        #print(lifetime_gross)

        release_section = self.driver.find_elements(By.XPATH,'//td[@class="a-text-left mojo-field-type-year"]/a[@class="a-link-normal"]')
        self.release_year = []
        for year in range(len(release_section)):
            self.release_year.append(release_section[year].text)
        #print(release_year)

    def load_csv(self):

        self.data =list(zip(self.movie_name, self.release_year, self.lifetime_gross))
        #create dataframe, dataset name ## columns names
        df_1 = pd.DataFrame(self.data,columns=['Movie Name','Release Date','Lifetime Earnings'])
        df_1.to_csv('top_movies.csv',index=False)


new_movie = movie()
print(movie.extract_data())
print(movie.load_csv())