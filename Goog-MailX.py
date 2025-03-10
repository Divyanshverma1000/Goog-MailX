#!/usr/bin/env python3
import re
import argparse
import sys
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Regular expression to match common email addresses
EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

def construct_search_url(domain, engine="bing", page_index=0):
    query = f"site:{domain} email"
    if engine == "google":
        # For Google, the pagination parameter is 'start'
        start = page_index * 10
        return f"https://www.google.com/search?q={query}&start={start}"
    elif engine == "bing":
        # For Bing, the pagination parameter is 'first'
        # First page: first=1; second: first=11; etc.
        first = page_index * 10 + 1
        return f"https://www.bing.com/search?q={query}&first={first}"
    else:
        raise ValueError(f"Unsupported search engine: {engine}")

def fetch_search_results_selenium(domain, engine="bing", proxy=None, debug=False, max_pages=3):
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Error initializing ChromeDriver: {e}")
        sys.exit(1)
    
    combined_content = ""
    for page in range(max_pages):
        url = construct_search_url(domain, engine, page_index=page)
        try:
            driver.get(url)
            time.sleep(3)  # Wait for JavaScript to load the content
            page_content = driver.page_source
            if debug:
                print(f"DEBUG: Page {page+1} URL: {url}")
                print("DEBUG: Fetched HTML content snippet:")
                print(page_content[:500])
            combined_content += page_content
        except Exception as e:
            print(f"Error fetching page {page+1}: {e}")
    
    driver.quit()
    return combined_content

def extract_emails(content):
    emails = re.findall(EMAIL_REGEX, content)
    return set(emails)

def output_emails(emails, output_type="text"):
    if output_type == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["email"])
        for email in emails:
            writer.writerow([email])
    else:
        for email in emails:
            print(email)

def main():
    parser = argparse.ArgumentParser(description="Goog-mail.py - Email Enumeration & OSINT Tool with Pagination using Selenium")
    parser.add_argument("domain", help="Domain to enumerate emails from (e.g., example.com)")
    parser.add_argument("-t", "--type", choices=["text", "csv"], default="text", help="Output format (default: text)")
    parser.add_argument("-e", "--engine", choices=["google", "bing"], default="bing", help="Search engine to use (default: bing)")
    parser.add_argument("--proxy", help="Optional proxy (e.g., http://127.0.0.1:8080)")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode to print HTML snippets")
    parser.add_argument("--max-pages", type=int, default=3, help="Maximum number of pages to fetch (default: 3)")
    args = parser.parse_args()

    content = fetch_search_results_selenium(args.domain, engine=args.engine, proxy=args.proxy, debug=args.debug, max_pages=args.max_pages)
    emails = extract_emails(content)
    
    if not emails:
        print("No emails found.")
    else:
        output_emails(emails, output_type=args.type)

if __name__ == "__main__":
    main()
