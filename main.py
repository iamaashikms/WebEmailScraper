from email_extractor import get_page_content, extract_emails
from decoders import decode_base64, decode_hex, decode_rot13
from selenium_scraper import get_email_with_selenium
from bs4 import BeautifulSoup

def main():
    url = 'ADD_THE_URL_HERE'
    page_content = get_page_content(url)
    
    if not page_content:
        return
    
    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text()
    
    extracted_emails = extract_emails(text)
    
    # Try decoding possible encoded emails while maintaining order
    decoded_emails = []
    for email in extracted_emails:
        decoded_email = decode_base64(email) or decode_hex(email) or decode_rot13(email) or email
        if decoded_email not in decoded_emails:
            decoded_emails.append(decoded_email)
    
    # Use Selenium if necessary, maintaining order
    selenium_emails = get_email_with_selenium(url)
    for email in selenium_emails:
        if email not in decoded_emails:
            decoded_emails.append(email)
    
    if decoded_emails:
        print("Emails found:")
        for email in decoded_emails:
            print(email)
    else:
        print("No emails found.")

if __name__ == "__main__":
    main()
