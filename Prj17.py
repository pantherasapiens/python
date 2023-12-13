# Not working
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the Chrome web driver
driver = webdriver.Chrome()

# Open WhatsApp Web URL
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

# Prompt user for contact information
contact_name = input("Enter the contact's name: ")
contact_number = input("Enter the contact's phone number (including country code): ")
message = input("Enter the message you want to send: ")

# Locate and clear the search box
search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
person_title = wait.until(lambda driver: driver.find_element_by_xpath(search_box))
person_title.clear()

# Send contact number to the search box
person_title.send_keys(contact_number)

# Wait for 2 seconds to search for the contact
time.sleep(2)

try:
    # Check for the presence of an error message
    error_message = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span')
except NoSuchElementException:
    # Format the message
    formatted_message = message.replace('{contact_name}', contact_name)

    # Press Enter to select the contact
    person_title.send_keys(Keys.ENTER)

    # Simulate key presses to send the message
    actions = ActionChains(driver)
    actions.send_keys(formatted_message)
    actions.send_keys(Keys.ENTER)
    actions.perform()

# Close the Chrome browser
driver.quit()
