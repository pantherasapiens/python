from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions

# Input the URL of the website you want to open
website_url = input("Enter the URL of the website you want to open:")

# Provide the full path to the chromedriver executable
chromedriver_path = '/path/to/chromedriver'

# Create ChromeOptions instance
chrome_options = Options()
chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')  # Set the WebDriver executable path

# Assigning the browser variable with chromedriver of Chrome
browser = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the specified website
    browser.get(website_url)

    # Optionally, you can perform actions on the website here.
    # For example, you can interact with elements on the webpage using Selenium functions.

    # Add a delay (optional) before interacting with the website
    # time.sleep(2)  # Wait for 2 seconds

except selenium.common.exceptions.WebDriverException as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser when done, even if an exception occurs
    # browser.quit()
    # Add a delay or loop to keep the script running
    input("Press Enter to close the browser and end the script...")

# Close the browser manually by closing the window.
    
