import os, requests, json, datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver/chromedriver')
driver.implicitly_wait(3)

startdate = '02152013'
# enddate = '04252023'
enddate = '04242023'

fpath = f"resource/expression.csv"

date = startdate

with open(fpath, 'a') as f:
    while date != enddate:

        print(date)

        # Go to the page
        url = f'https://www.koreanclass101.com/korean-phrases/{date}#wotd-widget'
        driver.get(url)
        driver.implicitly_wait(3)

        # Get the data
        expression = driver.find_elements(By.XPATH, '//*[@id="wotd-widget"]/div')[1:]

        flag = False
        ko_pr_en = {}
        for i, e in enumerate(expression):
            data = e.text.split('\n')
            print(data)
            if len(data) == 3:
                ko_pr_en[i] = {
                    'ko': data[0],
                    'pr': "",
                    'en': data[2]
                }
            elif len(data) == 2:
                ko_pr_en[i] = {
                    'ko': data[0],
                    'pr': "",
                    'en': data[1]
                }
            elif len(data) == 4:
                ko_pr_en[i] = {
                    'ko': data[0],
                    'pr': data[1],
                    'en': data[2]
                }
            else:
                print("Error")
                flag = True
                break

        # Update the date
        date = datetime.datetime.strptime(date, '%m%d%Y')
        date += datetime.timedelta(days=1)
        date = date.strftime('%m%d%Y')

        if flag:
            continue

        json_kopren = json.dumps(ko_pr_en, ensure_ascii=False)
        f.write(json_kopren)
        f.write('\n')



driver.quit()