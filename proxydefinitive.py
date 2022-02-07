from selenium import webdriver
from browsersettings import chrome_driver_binary,options,d
import time

driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options, desired_capabilities=d)

driver.get('http://proxydb.net/?protocol=socks5&anonlvl=4&min_uptime=75&max_response_time=5&country=')
time.sleep(2)

currentpriceusd = driver.find_elements_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[1]/a")
#currentstock = driver.find_elements_by_xpath("/html/body/div[1]/div[7]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[4]/div[1]/div/div[1]/div/span[1]")

print(currentpriceusd)