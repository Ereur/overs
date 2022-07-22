import undetected_chromedriver as uc
import time
import pickle

PATH = "/Users/aamoussa/Desktop/selenium/chromedriver"

if __name__ == '__main__':
	driver = uc.Chrome()

	driver.get("https://discord.com/login?redirect_to=%2Fchannels%2F788078738905628682%2F884398456641298472")
	time.sleep(50)
	cokie = driver.get_cookies()
	print(cokie)
	pickle.dump(cokie, open("discord_cokie.pkl", "wb"))
	time.sleep(60)