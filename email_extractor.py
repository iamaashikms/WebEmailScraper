import requests
import re

def get_page_content(url):
    """Fetch website content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def extract_emails(text):
    """Extract possible obfuscated emails from text in order."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)  # Preserve order
