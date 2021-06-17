import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)

driver.get("https://www.time-j.net/worldtime/country/jp")
driver.implicitly_wait(5)

print(driver.find_element_by_xpath("/html/body/div/div[6]/div[1]/div/p[5]").text)
driver.quit()
