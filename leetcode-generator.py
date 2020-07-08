from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from sys import argv
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

URL = argv[1]
EMAIL = ""
PASSWORD = ""
DRIVER_PATH = "C:\\Users\\John\\PycharmProjects\\untitled1\\src\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://leetcode.com/accounts/login/')
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="signin_btn"]/div/span'))
    )
except ElementNotVisibleException:
    driver.quit()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="id_login"]').send_keys(EMAIL)
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(PASSWORD)
driver.find_element_by_xpath('//*[@id="signin_btn"]/div/span').click()

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'trending-discuss-container'))
    )
except ElementNotVisibleException:
    driver.quit()
time.sleep(1)
driver.get(URL)

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'description__24sA'))
    )
except ElementNotVisibleException:
    driver.quit()
time.sleep(1)
description = driver.find_element_by_class_name('description__24sA')

title = '' + description.find_element_by_class_name('css-v3d350').text
titleSlug = '-'.join(title.replace('.', '').split(' '))

details = "" + description.find_element_by_class_name('question-content__JfgR').text

driver.find_element_by_class_name('ant-select-selection__rendered').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[7]').click()
time.sleep(0.5)
code = "" + driver.find_element_by_class_name('CodeMirror-lines').text
code = code.split('\n')
code = code[1::][::2]
code.pop()
code.append('')
code.append('};')
code = '\n'.join(code)

driver.close()

time.sleep(0.5)
os.chdir('C:\\Users\\John\\Documents\\Programming\\leetcode-javaScript')
time.sleep(0.5)
os.system('git checkout master')
time.sleep(0.5)
os.system('git checkout -b ' + titleSlug.lower())
time.sleep(0.5)
os.system('mkdir ' + titleSlug.lower())
time.sleep(0.5)
os.chdir('C:\\Users\\John\\Documents\\Programming\\leetcode-javascript\\'+titleSlug.lower())
time.sleep(0.5)
os.system('touch README.md')
time.sleep(0.5)
os.system('touch attempt1.js')

f = open("README.md", 'w')
f.write(URL)
f.write('\n\n')
f.write('<details>\n\n')
f.write('<summary>Question</summary>\n\n')
for line in details.split('\n'):
    f.write(line)
    f.write('\n\n')
f.write('</details>')
f.write('\n\n')
f.write('<details>\n')
f.write('<summary>Prompt</summary>\n')
f.write('\n\n')
f.write(code)
f.write('</details>\n\n')

f.write('<table>\n')
f.write('<thead>\n')
f.write('<tr>\n')
f.write('<th>Problem</th>\n')
f.write('<th>Date</th>\n')
f.write('<th>Time Complexity</th>\n')
f.write('<th>Space Complexity</th>\n')
f.write('<th>Time (minutes)</th>\n')
f.write('<th>Score</th>\n')
f.write('<th>Repeat Date</th>\n')
f.write('<th>Comments</th>\n')
f.write('</tr>\n')
f.write('</thead>\n')
f.write('<tbody>\n')
f.write('<tr>\n')
f.write('<td>'+URL+'</td>\n')
f.write('<td></td>\n')
f.write('<td></td>\n')
f.write('<td></td>\n')
f.write('<td></td>\n')
f.write('<td></td>\n')
f.write('<td></td>\n')
f.write('<td></td>\n')
f.write('</tr>>\n')
f.write('</tbody>\n')
f.write('</table>\n')
f.close()

f = open("attempt1.js", 'w')
f.write(code)
f.close()
