# Web Email Extractor

A Python tool to extract email addresses from web pages, including obfuscated and dynamically rendered emails. The Web Email Extractor supports multiple methods of extraction, ensuring that even emails hidden using encoding techniques (Base64, Hex, ROT13) or JavaScript rendering are successfully retrieved.

## Features

- **Extract emails**: Extracts emails from static HTML content using regex.
- **Decode obfuscated emails**: Handles Base64, Hex, and ROT13 encoding schemes to decode emails.
- **Dynamic content extraction**: Uses Selenium to extract emails from dynamically generated content (such as JavaScript-rendered links).
- **Preserve order**: Maintains the order of emails as they appear on the webpage.
  
## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `selenium`
- `chromedriver` (for Selenium)
  
### Installing the required dependencies

To install the necessary libraries, use `pip`:

```bash
pip install requests beautifulsoup4 selenium
