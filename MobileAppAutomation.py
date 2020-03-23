from appium import webdriver

desiredCapabilities = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.sand.airmirror",
  "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_",
  "app": "C:\\Users\\105608\\Downloads\\devices_v1.0.5.2_apkpure.com.apk",
  "automationName": "UiAutomator1"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredCapabilities)

driver.find_element_by_id('com.sand.airmirror:id/tvRegister').click()
driver.find_element_by_xpath("//*[@text='Email']").send_keys('shubhojit.bhattacharjee@gmail.com')
driver.find_element_by_xpath("//*[@text='Password']").send_keys('test1234')
driver.find_element_by_xpath("//*[@text='Enter password again']").send_keys('test1234')
driver.find_element_by_xpath("//*[@text='Nick name']").send_keys('test nick name')

driver.find_element_by_id('com.sand.airmirror:id/btnRegister').click()
