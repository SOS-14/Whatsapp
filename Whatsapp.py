import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

s = webdriver.Chrome(ChromeDriverManager().install())
s.get('https://web.whatsapp.com/')
input('After scan the QR:')
name = str(input('Enter the name of chat: \n'))
massage = str(input('Enter the message u want: \n'))

user = s.find_element(By.XPATH, '//span[@title = "{name_of_chat}"]'.format(name_of_chat="name"))
user.click()

mass = s.find_element(By.XPATH, '//div[@class="_2vbn4"]')

def sos():
    while True:
        for i in range(10):
            #                    time of message
            WebDriverWait(s, 5)
            t = s.find_elements(By.XPATH, '//div[@class="_1beEj"]')
            time.sleep(10)
            for r in t:
                time11 = r.text
                              # last context message
            message1 = s.find_elements(By.XPATH, '//div[@class="_1Gy50"]')
            for momo in message1:
                message = momo.text
            #                   to convert time to string
            time_message = str(time11[0:1] + ':' + time11[2:4] + ':00')
            date_now = str(datetime.now())
            time_now = date_now[11:13] + ':' + date_now[14:16] + ':00'
            #               to see the time of message and current time
            'just to test the time ||'
            print('time now: ', time_now)
            'just to test the time ||'
            print('time of last message: ', time_message)
            date_format_str = '%H:%M:%S'
            start = datetime.strptime(time_message, date_format_str)
            end = datetime.strptime(time_now, date_format_str)
            if end > start:
                diff = end - start
            else:
                diff = start - end
            diff_in_hours = math.floor(diff.total_seconds() / 60)
            #               to see the diffrent betweent two time
            # print('Difference between two datetimes in min:')
            print('Difference between two datetimes in min: {} '.format(diff_in_hours))
            #                   to send a message
            if diff_in_hours 'here you can put any sign u want == or > or < to match with the number of hours' , 'the number of hours you want':
                ActionChains(s).move_to_element(mass).send_keys('PING').perform()
                button = s.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
                button.click()

sos()
