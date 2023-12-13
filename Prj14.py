from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse
import selenium.common.exceptions
# import time

# Taking input from the user
search_string = input("Input the URL or string you want to search for:")

# Properly encode the search string for the URL
search_string = urllib.parse.quote(search_string)

# Provide the full path to the chromedriver executable
chromedriver_path = '/path/to/chromedriver'

# Create ChromeOptions instance
chrome_options = Options()
chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')  # Set the WebDriver executable path

# Assigning the browser variable with chromedriver of Chrome
browser = webdriver.Chrome(options=chrome_options)

# Define the number of pages of search results to scrape
num_pages_to_scrape = 5

# Loop through multiple pages of search results
for i in range(num_pages_to_scrape):
    # Create the search URL with page number
    search_url = f"https://www.google.com/search?q={search_string}&start={i*10}"

    try:
        # Navigate to the search URL
        browser.get(search_url)

        # Perform web scraping or data extraction here
        # You can extract information from the search results page
        # using Selenium functions like find_element_by_xpath, find_element_by_class_name, etc.

        # Add a delay (optional) before interacting with the browser
        # time.sleep(2)  # Wait for 2 seconds

    except selenium.common.exceptions.NoSuchWindowException:
        print("The browser window has been closed.")
        break  # Exit the loop if the window is closed

# Close the browser when done
browser.quit()
