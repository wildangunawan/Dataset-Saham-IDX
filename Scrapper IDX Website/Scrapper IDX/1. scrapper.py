from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta

# Define the initial date in the format "YYYYMMDD"
start_date_str = "20230524"

# Convert the start date string to a datetime object
start_date = datetime.strptime(start_date_str, "%Y%m%d")

# Define the end date by subtracting the desired days from the start date
end_date = start_date - timedelta(days=2)

# Open a text file for writing
dateRange = []
current_date = start_date
while current_date >= end_date:
    # Convert the current date to the desired format
    current_date_str = current_date.strftime("%Y%m%d")

    # Write the current date to the text file
    dateRange.append(current_date_str)

    # Move to the previous date
    current_date -= timedelta(days=1)

# Set up Chrome WebDriver
driver = webdriver.Chrome('/path/to/chromedriver')
file = open('website_content_2days.txt', 'w', encoding='utf-8')

for date in dateRange:
    url = f"https://idx.co.id/primary/TradingSummary/GetStockSummary?length=9999&start=0&date={date}"
    driver.get(url)

    # Wait for the page to fully load 
    driver.implicitly_wait(1)

    # Only get element in body
    content = driver.find_element(By.XPATH, '//body').text

    # write it to a file
    file.write(content)
driver.quit()

# clean the data
