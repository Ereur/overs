import undetected_chromedriver as uc
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

PATH = "/workspace/leetmove/selinuim/chromedriver"
dict = {}
if __name__ == '__main__':
    uc.install(
    executable_path="/workspace/leetmove/selinuim/chromedriver",
    )
    opts = uc.ChromeOptions()
    opts.headless = True
    # opts.add_argument(f'--proxy-server=socks5://127.0.0.1:9050')
    driver = uc.Chrome(options=opts)
    driver.get("https://overseer.1337.ma/user/122")
    cookies = pickle.load(open("cokie.pkl", "rb"))
    print(cookies);
    for cookie in cookies :
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.get("https://overseer.1337.ma/user/122")
    time_spent = driver.find_element(By.ID , "__next")
    text = time_spent.text
    print(text);
    exit()
    result = text.split('\n')
    time_spent = result[5].replace(' days were spent on the common core', '')
    dict['time_spent'] = time_spent
    json_object = json.dumps(dict, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    # driver.get("https://discord.com/channels/788078738905628682/884398456641298472")
    # cookies = pickle.load(open("discord_cokie.pkl", "rb"))
    # for cookie in cookies :
    #     driver.add_cookie(cookie)
    # driver.get("https://discord.com/channels/788078738905628682/884398456641298472")
    time.sleep(60)

    
