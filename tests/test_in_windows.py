from selenium import webdriver

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('../lib/chromedriver', options=options)

driver.get('https://google.com')
assert 'Google' in driver.title
driver.find_element_by_name('q').send_keys("Browser Automation")

driver.quit()