import os
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

USERNAME = "aliceinspace._"
PASSWORD = "3712281zjLF"
CHAT_LINK = "https://www.instagram.com/direct/t/17842106975322348/"
MESSAGE = "hi"

# Path to your chromedriver
# CHROMEDRIVER_PATH = "/path/to/chromedriver"
def send_instagram_message():
    driver = webdriver.Chrome(
        # service=ChromeService(CHROMEDRIVER_PATH), options=chrome_options
    )
    driver.get("https://www.instagram.com")

    # Log in to Instagram
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(5)
    
    save_info_button = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37[role="button"][tabindex="0"]')
    save_info_button.click()
    time.sleep(5)

    notif_button = driver.find_element(By.CSS_SELECTOR, 'button._a9--._ap36._a9_1[tabindex="0"]')
    notif_button.click()

    # Navigate to chat link
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/direct/inbox/']")))
    driver.get(CHAT_LINK)
    time.sleep(6)

    # Send the message
    message_box = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Message']")
    message_box.clear()
    message_box.send_keys(MESSAGE)
    message_box.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.close()

if __name__ == "__main__":
    send_instagram_message()
