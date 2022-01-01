from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager


ops = Options()
ops.add_argument("--headless") # żeby interfejsu nie otwierało
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=ops)