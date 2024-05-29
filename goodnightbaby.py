import os
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

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
CHAT_LINK = os.getenv("CHAT_LINK")
MESSAGE = os.getenv("MESSAGE")

# Set up Chrome options for Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Path to your chromedriver
CHROMEDRIVER_PATH = "/path/to/chromedriver"

def send_instagram_message():
    driver = webdriver.Chrome(service=ChromeService(CHROMEDRIVER_PATH), options=chrome_options)
    driver.get("https://www.instagram.com")

    # Log in to Instagram
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    # Navigate to chat link
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/direct/inbox/']")))
    driver.get(CHAT_LINK)

    # Send the message
    message_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    message_box.send_keys(MESSAGE)
    message_box.send_keys(Keys.RETURN)

    driver.quit()

# Uncomment if running locally with schedule
# schedule.every().day.at("23:00").do(send_instagram_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == "__main__":
    send_instagram_message()
