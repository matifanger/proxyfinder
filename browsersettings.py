from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Browser settings
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
options = webdriver.ChromeOptions()

# Browser arguments
#options.add_argument('--headless')

# Browser binaries
options.binary_location = r"D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Python27\chromedriver"