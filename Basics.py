from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser='ff'
if(browser=='chrome'):
  driver=webdriver.Chrome(executable_path="C:/Program Files/chromedriver.exe")
elif(browser=='ff'):
   driver=webdriver.Firefox(executable_path="C:/Users/MadhusmitaPanda/Documents/geckodriver.exe")
elif(browser=='ie'):
    driver = webdriver.Ie(executable_path="C:/Users/MadhusmitaPanda/Documents/IEDriverServer.exe")
driver.get("http://www.facebook.com")
driver.implicitly_wait(30)
driver.find_element_by_name("firstname").send_keys("madhu")
driver.find_element_by_name("lastname").send_keys("smita")
# driver.find_element_by_name("reg_email__").send_keys("3245678678")
driver.find_element_by_xpath("//input[contains(@aria-label,'Mobile number')]").send_keys("3245678678")
driver.find_element_by_xpath("//input[@aria-label='New password']").send_keys("Madhu@2019")
selctvalue=Select(driver.find_element_by_id('day'))
selctvalue.select_by_value('6')
# selctvalue1=Select(driver.find_element_by_id('month'))
# selctvalue1.select_by_value('jun')
# selctvalue2=Select(driver.find_element_by_id('year'))
# selctvalue2.select_by_value('1992')
driver.find_element_by_xpath("//input[@value='1']").click()
driver.find_element_by_name("websubmit").click()

# driver.__exit__()
