from selenium import webdriver
from selenium.webdriver.common.by import By

def get_email_with_selenium(url):
    """Use Selenium to extract dynamically decoded emails in order."""
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        email_elements = driver.find_elements(By.TAG_NAME, "a")
        emails = [elem.get_attribute("href") for elem in email_elements if elem.get_attribute("href") and "mailto:" in elem.get_attribute("href")]
        driver.quit()
        return [email.replace("mailto:", "") for email in emails]
    except Exception as e:
        print(f"Selenium error: {e}")
        return []
