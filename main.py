#install selenium using command "pip install -r requirements.txt" on command terminal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random,time
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Enter username and password
user=str(input('Username: '))
pswd=str(input('Password: '))
#List of Recievers
receiver=[]

#define text file to open
my_file = open('accounts.txt', 'r')
#read text file into list
receiver = my_file.read().split()
#Select the driver, In our case we will use Chrome.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

s=Service('Chromedriver PATH')
#Message you want to send along with the post
message=str(input('Message you want to send along with the post: '))
#Time taken between messages to different users
between_messages = 2
#Log-in Function
def auth(username, password):
    try:
        
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2,4))
        #Entering username ,password
        input_username = browser.find_element(By.NAME,'username')
        input_password = browser.find_element(By.NAME,'password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1,2))
        #Logging in
        input_password.send_keys(Keys.ENTER)
        #browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
        time.sleep(random.randrange(3,5))


    except Exception as err:
        print("Did not log in")
        print("Could not log in./n Retry")
        browser.quit()

# Sending posts:
def send_post(users, messages):
    try:
        #Notnow1
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
        time.sleep(random.randrange(3,5))
    except Exception as err:
        print("Other variate")

    try:
        #Notnow2
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()	
        time.sleep(random.randrange(3,5))
        #Profile button
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div/div[1]').click()
        time.sleep(random.randrange(3,4))
        #Selecting most recent post
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div').click()
        time.sleep(random.randrange(3,4))
        #Share button
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[3]/button').click()
        time.sleep(random.randrange(3,4))
        #Entering user names
        for user in users:
            browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(random.randrange(3,4))
            browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]').click()#find_element(By.TAG_NAME,'button').click()
            time.sleep(random.randrange(3,4))
            print(f'Message sent to {user}')
        #Entering message in messaging area
        text_area = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[3]/input')
        text_area.send_keys(messages)
        time.sleep(random.randrange(3,5))
        #Sending post 
        browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[4]/button').click()
        time.sleep(random.randrange(3,4))
        
    except Exception as err:
        print(err)
        print("Could not send post")
        browser.quit()



#Info
auth(user, pswd)
time.sleep(random.randrange(2,4))
send_post(receiver, message)
