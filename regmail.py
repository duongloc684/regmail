from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
sleep(1)


###-----------------name--------------###
firstname ="name/ho.txt"
lastname = "name/ten.txt"
file_1 = open(firstname, "r",encoding="utf8").readlines()
file_2 = open(lastname, "r",encoding="utf8").readlines()
# print(file_1[random.randint(0,20)])
rd_1 = file_1[random.randint(0,155)]
rd_2 = file_2[random.randint(0,211)]


crd_1 = rd_1.strip()
crd_2 = rd_2.strip()
pl = crd_1 + crd_2 + str(random.randint(111111111,999999999))
print(rd_1)
print(rd_2)
###-----------------name--------------###

###-----------------password--------------###
random_pass = ''
rd_pass = "qwertyuiopasdfghjklzxcvbnm0123456789"

for i in range(10):
 random_pass += rd_pass[random.randint(0, 35)]
print(random_pass)
###-----------------password--------------###



driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
sleep(5)

driver.find_element('id', 'lastName').send_keys(rd_1)
sleep(2)
driver.find_element('id', 'firstName').send_keys(rd_2)
sleep(3)

driver.find_element('id', 'day').send_keys(random.randint(1,30))
sleep(2)

select = Select(driver.find_element('id', 'month'))
select.select_by_value(str(random.randint(1,12)))
sleep(2)

driver.find_element('id', 'year').send_keys(random.randint(1975,2005))
sleep(2)

select = Select(driver.find_element('id', 'gender'))
select.select_by_value(str(random.randint(1,3)))
sleep(2)

driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/span').click()
sleep(2)


driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[3]/div/div[1]/div/div[3]/div').click()
sleep(2)

driver.find_element('name','Username').send_keys(pl)

driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
sleep(2)

driver.find_element('name','Passwd').send_keys(random_pass)
sleep(1)
driver.find_element('name','PasswdAgain').send_keys(random_pass)

with open("account/list.txt", "a+")as fp:
 fp.write('\n')
 fp.write(pl + '|' + random_pass)

sleep(100)

# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/input").click