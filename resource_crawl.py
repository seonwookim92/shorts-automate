xpath = {
    'naver_dict':{
        'vocab1':{
            'ko_word': '//*[@id="content"]/div[3]/div[1]/div/div/div[2]/div/div/div[2]/a',
            'en_mean': '//*[@id="content"]/div[3]/div[1]/div/div/div[2]/div/div/div[3]/span',
            'ko_sound': '//*[@id="content"]/div[3]/div[1]/div/div/div[2]/div/div/div[2]/button'
        },
        'vocab2':{
            'ko_word': '//*[@id="content"]/div[3]/div[1]/div/div/div[3]/div/div/div[2]/a',
            'en_mean': '//*[@id="content"]/div[3]/div[1]/div/div/div[3]/div/div/div[3]/span',
            'ko_sound': '//*[@id="content"]/div[3]/div[1]/div/div/div[3]/div/div/div[2]/button'
        
        },
        'conversation':{
            'ko_sentence': '//*[@id="todayQuiz"]/div/div/div[1]',
            'en_translate': '//*[@id="todayQuiz"]/div/div/div[2]/p'
        },
        'idiom1':{
            'ko_idiom': '//*[@id="content"]/div[5]/div/div/div/div[2]/div/div/div[1]/a',
            'en_mean': '//*[@id="content"]/div[5]/div/div/div/div[2]/div/div/div[2]'
        },
        'idiom2':{
            'ko_idiom': '//*[@id="content"]/div[5]/div/div/div/div[3]/div/div/div[1]/a',
            'en_mean': '//*[@id="content"]/div[5]/div/div/div/div[3]/div/div/div[2]',
        },
        'idiom3':{
            'ko_idiom': '//*[@id="content"]/div[5]/div/div/div/div[4]/div/div/div[1]/a',
            'en_mean': '//*[@id="content"]/div[5]/div/div/div/div[4]/div/div/div[2]',
        },
        'idiom4':{
            'ko_idiom': '//*[@id="content"]/div[5]/div/div/div/div[5]/div/div/div[1]/a',
            'en_mean': '//*[@id="content"]/div[5]/div/div/div/div[5]/div/div/div[2]',
        },
        'idiom5':{
            'ko_idiom': '//*[@id="content"]/div[5]/div/div/div/div[6]/div/div/div[1]/a',
            'en_mean': '//*[@id="content"]/div[5]/div/div/div/div[6]/div/div/div[2]',
        },
        'food1':{
            'ko_food': '//*[@id="content"]/div[6]/div/div/div[1]/div/a',
            'en_mean': '//*[@id="content"]/div[6]/div/div/div[1]/ul/li/p',
            'img': '//*[@id="content"]/div[6]/div/div/div[1]/div/div/img'
        },
        'food2':{
            'ko_food': '//*[@id="content"]/div[6]/div/div/div[2]/div/a',
            'en_mean': '//*[@id="content"]/div[6]/div/div/div[2]/ul/li/p',
            'img': '//*[@id="content"]/div[6]/div/div/div[2]/div/div/img'
        }
    },
    'koreanclass101':{
        'table': '//*[@id="wotd-widget"]/div'
    }
}

filename = {
    'sentence': 'sentence.csv',
    'idiom': 'idiom.csv',
    'food': 'food.csv',
    'vocab': 'vocab.csv',
    'expression': 'expression.csv'
}

import os, requests, json

# mp3_url = 'https://dict-dn.pstatic.net/v?_lsu_sa_=3f485e584d7837961b97416c33d458f26da469a5e000df7c678237750b4a6841db5a876469057479294d60b53c244070990b83dd8f49e5a2ae6d018c33afb4c83d912c500a421fde17b22d162457178ecce25f516dfecc3a3f9b6ca0909ed3d5bb1aeb7f99a1cd4d9565c87a4672c80c01deca84cc5c6e53ba6f7954027159bd'

# # Download from the URL
# r = requests.get(mp3_url, allow_redirects=True)
# open('v1.mp3', 'wb').write(r.content)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver/chromedriver')
driver.implicitly_wait(3)

# url1 = 'https://korean.dict.naver.com/koendict/#/main'

# driver.get(url1)

# conversation = [driver.find_element(By.XPATH, xpath['naver_dict']['conversation']['ko_sentence']).text, driver.find_element(By.XPATH, xpath['conversation']['en_translate']).text]
# idiom1 = [driver.find_element(By.XPATH, xpath['naver_dict']['idiom1']['ko_idiom']).text, driver.find_element(By.XPATH, xpath['idiom1']['en_mean']).text]
# # idiom2 = [driver.find_element(By.XPATH, xpath['naver_dict']['idiom2']['ko_idiom']).text, driver.find_element(By.XPATH, xpath['idiom2']['en_mean']).text]
# # idiom3 = [driver.find_element(By.XPATH, xpath['naver_dict']['idiom3']['ko_idiom']).text, driver.find_element(By.XPATH, xpath['idiom3']['en_mean']).text]
# # idiom4 = [driver.find_element(By.XPATH, xpath['naver_dict']['idiom4']['ko_idiom']).text, driver.find_element(By.XPATH, xpath['idiom4']['en_mean']).text]
# # idiom5 = [driver.find_element(By.XPATH, xpath['naver_dict']['idiom5']['ko_idiom']).text, driver.find_element(By.XPATH, xpath['idiom5']['en_mean']).text]
# food1 = [driver.find_element(By.XPATH, xpath['naver_dict']['food1']['ko_food']).text, driver.find_element(By.XPATH, xpath['food1']['en_mean']).text, driver.find_element(By.XPATH, xpath['food1']['img']).get_attribute('src')]
# food2 = [driver.find_element(By.XPATH, xpath['naver_dict']['food2']['ko_food']).text, driver.find_element(By.XPATH, xpath['food2']['en_mean']).text, driver.find_element(By.XPATH, xpath['food2']['img']).get_attribute('src')]



url2 = 'https://www.koreanclass101.com/korean-phrases'

driver.get(url2)

expression = driver.find_elements(By.XPATH, xpath['koreanclass101']['table'])[1:]

fpath = f"resource/{filename['expression']}"

ko_pr_en = {}
for i, e in enumerate(expression):
    data = e.text.split('\n')
    ko_pr_en[i] = {
        'ko': data[0],
        'pr': data[1],
        'en': data[2]
    }


json_kopren = json.dumps(ko_pr_en, ensure_ascii=False)
with open(fpath, 'a') as f:
    f.write(json_kopren)