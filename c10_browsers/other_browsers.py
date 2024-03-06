from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver.core.utils import ChromeType
from webdriver.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
#CHROME
# petru a rula teste pe Chrome, cu versiunea de selnium 4.6.0+
chrome = webdriver.Chrome()
# pentru a rula teste pe Chrome cu o versiune mai veche de selenium 4.6.0
# chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Firefox
# petru a rula teste pe Firefox, cu versiunea de selnium 4.6.0+
driver = webdriver.Firefox()

# pentru a rula teste pe Firefox cu o versiune mai veche de selenium 4.6.0
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#Brave
# driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))




driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element(By.ID,"first-name").send_keys("TEST")

sleep(5)

driver.quit()
