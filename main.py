import time
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

login = input("Введите ваш логин от сайта госуслуг: ")
password = input("Введите ваш пароль от сайта госуслуг: ")
chromedriver = "/home/twocb/Downloads/chromedriver"  # point to chromedriver location
driver = webdriver.Chrome(executable_path=chromedriver)
driver.get('https://esia.gosuslugi.ru/')  # go to gosuslugi.ru login page
time.sleep(1)  # wait for page was loaded
login_form = driver.find_element(By.CSS_SELECTOR, "#login")  # find login form
login_form.send_keys(login)  # enter login data
password_form = driver.find_element(By.CSS_SELECTOR, "#password")  # find password form
password_form.send_keys(password)  # enter password data
submit_button = driver.find_element(By.CSS_SELECTOR, "#loginByPwdButton")  # find submit button
submit_button.click()  # click submit button

driver.get('https://lk.gosuslugi.ru/profile/id-doc')  # go to passport data page

if not os.path.exists('ids'):
    os.mkdir('ids')
else:
    pass

time.sleep(1)

# scrape passport data from page
name = driver.find_element(By.XPATH,
                           '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/'
                           'lk-doc-card/section/div/div[1]/h4').text
gender = driver.find_element(By.XPATH,
                             '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                             'section/div/div[2]/div[1]/lk-doc-card-row/div/div[2]').text
birth_date = driver.find_element(By.XPATH,
                                 '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                                 'section/div/div[2]/div[2]/lk-doc-card-row/div/div[2]').text
citizenship = driver.find_element(By.XPATH,
                                  '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                                  'section/div/div[2]/lk-doc-card-row/div/div[2]').text
birth_place = driver.find_element(By.XPATH,
                                  '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                                  'section/div/lk-doc-card-row[1]/div/div[2]').text
number_id = driver.find_element(By.XPATH,
                                '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                                'section/div/div[4]/h4').text
issued = driver.find_element(By.XPATH,
                             '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                             'section/div/lk-doc-card-row[2]/div/div[2]').text
date_of_issue = driver.find_element(By.XPATH,
                                    '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                                    'section/div/div[5]/div/lk-doc-card-row/div/div[2]').text
department_code = driver.find_element(By.XPATH,
                                      '/html/body/lk-root/main/ng-component/div/lk-rf-passport/div[2]/lk-doc-card/'
                                      'section/div/div[5]/lk-doc-card-row/div/div[2]').text

# open csv file and write data in
with open('ids/data', 'a+') as f:
    # create the csv writer
    writer = csv.writer(f)
    data = [name, birth_date, gender, citizenship, birth_place, number_id, issued, date_of_issue, department_code]
    # write a row to the csv file
    writer.writerow(data)

driver.close()
