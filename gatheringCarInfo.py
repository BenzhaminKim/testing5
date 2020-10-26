from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://e-insmarket.or.kr/aimt/aimtRealIntro.knia")

def clickAllAgreeButton():
    try:
        allTermAgreeButton = driver.find_element_by_xpath('//*[@id="allTermAgreeButton"]')
        allTermAgreeButton.click()
    except:
        return False
    return True

