from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

file=pd.read_excel("200.xlsx")

for index,item in file.iterrows():
    driver=webdriver.Chrome(r"C:\Users\Azure\Downloads\Mehul\Installations\chromedriver.exe")
    driver.get("https://woobox.com/hhr94u/o2pmvv")

    first=driver.find_element_by_id("custom_2_first")
    last=driver.find_element_by_id("custom_2_last")
    mobile=driver.find_element_by_id("mobile_no_id")
    email=driver.find_element_by_id("email_id")
    button1=driver.find_element_by_id("actionbutton")
    button2=driver.find_element_by_xpath("//*[@id=\"choice_41\"]/div[3]")

    button2.click()
    first.send_keys(item['First'])
    last.send_keys(item['Last'])
    mobile.send_keys(item['Mobile'])
    email.send_keys(item['Email'])
    button1.click()
    driver.close()
    



