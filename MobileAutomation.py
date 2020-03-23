from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')

driver = webdriver.Chrome('./lib/chromedriver', options=options)

driver.get('https://google.com')
driver.find_element_by_xpath("//*[contains(text(), 'Weather')]").click()
print(driver.find_element_by_id('wob_loc').text)
driver.quit()