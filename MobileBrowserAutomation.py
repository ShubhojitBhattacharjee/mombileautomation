from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'Android SDK built for x86',
    'udid': 'emulator-5554',
    'browserName': 'Chrome',
    'chromedriverExecutable': './lib/chromedriver'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)
driver.get('https://www.google.co.in/')

assert 'Google' in driver.title
assert driver.find_element_by_id('hplogo').is_displayed() is True

driver.find_element_by_xpath("//*[contains(text(), 'Weather')]").click()
print(driver.find_element_by_id('wob_loc').text)