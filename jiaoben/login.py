from selenium import webdriver#导入第三方selenium
from time import sleep
from selenium.webdriver.common.keys import Keys#a标签的点击方式
driver=webdriver.Firefox()
driver.get('http://132.232.9.93:9999/')

#driver.maximize_window()  浏览器最大化

#登录
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[2]/input').send_keys('123456@qq.com')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[3]/input').send_keys('123456')
sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/button').click()

#新建项目
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/a').send_keys(Keys.ENTER)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[1]/input').send_keys('tesr python selenium')

#input下拉框
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/span/span/i').click()
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]/span').click()

driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[3]/textarea').send_keys('测试用python创建datacenter的new project')
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/a[1]').send_keys(Keys.ENTER)



