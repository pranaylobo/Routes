import requests
import polyline
from flask import jsonify
from flask import Flask
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

app = Flask(__name__)
CORS(app)

@app.route('/reminder',methods=['GET'])
def main():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("/app/.apt/usr/bin/google-chrome")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("/app/.chromedriver/bin/chromedriver"), chrome_options=chrome_options)


    # driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.cowin.gov.in/home")
    
    print(driver.title)
    search_bar = driver.find_element_by_id("mat-input-0")
    # search_bar.clear()

    
  
    search_bar.send_keys("400068")
    search_bar.send_keys(Keys.RETURN)


    # slots-box
    # searchResults = driver.find_elements_by_class_name('vaccine-box1')
    raw = driver.find_elements(By.XPATH, "/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[7]")


    arr=['DAHISAR COVID JUMBO -10 Dahisar, Mumbai, Maharashtra, 400068 NA NA Booked COVISHIELD Age 45+ NA NA NA NA DAHISAR COVID JUMBO -8 Dahisar, Mumbai, Maharashtra, 400068 NA NA Booked COVISHIELD Age 45+ NA NA NA NA DAHISAR COVID JUMBO 1 Dahisar, Mumbai, Maharashtra, 400068 Booked COVISHIELD Age 45+ NA NA NA NA NA NA DAHISAR COVID JUMBO 6 Dahisar, Mumbai, Maharashtra, 400068 NA NA Booked COVISHIELD Age 45+ NA NA NA NA MEENATAI THAKRE MKT WARD NO. 4 Meenatai Thakre Market Sant Ghadge Maharaj Marg Rawalpada Dahisar East Mumbai, Mumbai, Maharashtra, 400068 Booked COVISHIELD Age 45+ NA NA NA NA NA NA SAMAJ KALYAN HALL WARD NO. 2 Samaj Kalyan Hall Near DSF Ground C. S. Main Road Dahisar East Mumbai, Mumbai, Maharashtra, 400068 Booked COVISHIELD Age 45+ NA NA NA NA NA NA']
    
    arr2=[]
    arr3=[]
    for x in raw:
        arr2.append(x.text)
        arr3 = arr2[0].replace("\n"," ")

    print(len(arr3))

    # if len(arr) is not "":

   
    
    if len(arr3) >0:
        if arr[0] == arr3:
            print("No Vaccine")
            

            driver.close()
            time.sleep(300)

            main()

            
        else:
            print("Vaccine")
            x = requests.get('https://emailserver12.herokuapp.com/email')
            

            print(x.text)

    else:
        main()

    

    
    return jsonify("Success")





if __name__ == '__main__':
   app.run()
