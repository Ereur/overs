import undetected_chromedriver as uc
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

PATH = "/Users/aamoussa/Desktop/selenium/chromedriver"

if __name__ == '__main__':
    uc.install(
    executable_path="/workspace/leetmove/selinuim/chromedriver",
    )
    opts = uc.ChromeOptions()
    opts.headless = True
    # opts.add_argument(f'--proxy-server=socks5://127.0.0.1:9050')
    driver = uc.Chrome(options=opts)
    driver.get("https://overseer.1337.ma/user/122")
    # driver.find_element_by_link_text('Login with Intra').click()
    time.sleep(5);
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(30)
    test = driver.find_element(By.ID , "__next")
    text = test.text
    print(text)
    cookies = pickle.load(open("cokie.pkl", "rb"))
    # print(cookies);
    # print(cokie)
    # pickle.dump(cokie, open("cokie.pkl", "wb"))
    time.sleep(60)

