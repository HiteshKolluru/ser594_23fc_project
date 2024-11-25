from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
chrome_service = Service("path/to/chromedriver")  # Update path to your WebDriver

# Billboard Hot 100 URL
url = "https://www.billboard.com/charts/hot-100/"

# Initialize WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get(url)

# Extract song and artist names
try:
    chart_items = driver.find_elements(By.CLASS_NAME, "o-chart-results-list__item")
    for item in chart_items[:10]:  # Adjust for the top 10 songs or more
        song = item.find_element(By.CSS_SELECTOR, ".c-title").text
        artist = item.find_element(By.CSS_SELECTOR, ".c-label").text
        print(f"Song: {song}, Artist: {artist}")
finally:
    driver.quit()
