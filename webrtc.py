# Created By Samer Mahafza
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


bots = {"lenny": "*0",
 "FitnessGram" : "*1",
 "Mack": "*2",
 "Egg Man": "*3",
 "Barry": "*4",
 "Posh man": "*5",
 "The Scientist": "*6",
 "Karen": "*7" ,
 "Medical Alert": "*8",
 "Y U CALL HERE": "*9",
 "Yes Bot": "0*",
 "Rohim": "**",
 "Bonzai Buddy": "88",
 "Tunak Tunak": "77",
 "Nadia": "66",
 "Mario Kart": "11",
 "Rickroll": "22",
 "Careless Whisper": "99",
 "Male Hindi": "55",
 "Female Hindi": "44",
 "Dr. Doofenshmirtz": "33",
}

symbol_xpath = { "1": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[1]',
 "2": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[2]',
 "3": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[3]',
 "4": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[4]',
 "5": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[5]',
 "6": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[6]',
 "7": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[7]',
 "8": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[8]',
 "9": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[9]', 
 "0": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[11]',
 "*": '//*[@id="cards"]/div[1]/div/div[2]/div[3]/ul/li[10]',
}

# change theese to your account information
email = "email goes here"
password = "password goes here"

driver = webdriver.Chrome()

driver.get("https://bobrtc.tel/phonebook/dial/18882235133")

time.sleep(5)

# remove these lines if you want to login manually
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(password + Keys.ENTER)


input("hit enter after login to discord")

driver.get("https://bobrtc.tel/phonebook/dial/18882235133")

first_press = 0
still_minute = False
hung_up = False
num_of_calls = 0

#variables to activate things
time_stamp_hungup = "00:01:00" # time to hungup
time_stamp_bot = "00:00:14" # time to choose bot

bot_name = "Y U CALL HERE"


def check_hung_up():
    global hung_up
    connect_check_status = driver.find_element_by_xpath('//*[@id="dialstatus"]').text
    if "Hung Up" in str(connect_check_status):
        hung_up = True
          


while True:
    try:
        connect_check_status = driver.find_element_by_xpath('//*[@id="dialstatus"]').text
    except Exception as e:
        pass
        
    if "Connected" in str(connect_check_status) and first_press == 0:
        num_of_calls +=1
        print("Called so far: {}".format(num_of_calls))
        still_minute = False
        while str(driver.find_element_by_xpath('//*[@id="clock"]').text) != time_stamp_bot and not hung_up:
            check_hung_up()
            
        if(not hung_up):
            try:
                driver.find_element_by_xpath(symbol_xpath[bots[bot_name][0]]).click()
            except:
                pass
            time.sleep(.5)
            try:
                driver.find_element_by_xpath(symbol_xpath[bots[bot_name][1]]).click()
            except:
                pass
            driver.execute_script("window.scrollTo(0, 0);")
            first_press = 1
        
    if "Hung Up" in str(connect_check_status) or str(driver.find_element_by_xpath('//*[@id="clock"]').text) == time_stamp_hungup and not still_minute:
        print("Calling again")
        still_minute = True
        driver.execute_script("window.scrollTo(0, 0);")
        driver.find_element_by_xpath('//*[@id="call"]').click()
        first_press = 0
        hung_up = False
        
    
             
