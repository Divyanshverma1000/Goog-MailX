# Goog-MailX 🚀

Goog-MailX is a powerful **OSINT (Open-Source Intelligence) email enumeration tool** that scrapes publicly available email addresses from search engine results. Using **Selenium**, it dynamically fetches content and extracts emails efficiently.  

## Features  
✅ **Supports Google & Bing** for searching emails from a domain  
✅ **Headless browsing** for automated extraction  
✅ **Pagination support** to retrieve more results  
✅ **Proxy support** for anonymity  
✅ **Customizable output format** (text/CSV)  
✅ **Debug mode** to inspect HTML content  

---

## Installation  

### Prerequisites  
Ensure you have the following installed on your system:  
- Python 3.x  
- Google Chrome (Latest version)  
- ChromeDriver (matching your Chrome version)  

You can install the required Python dependencies using:  
```bash
pip install selenium argparse
```

---

## Usage  

### Basic Command:  
```bash
python goog-mailx.py example.com
```
This will search for emails on **example.com** using Bing (default).  

### Advanced Usage:  

#### Specify Search Engine (Google or Bing)
```bash
python goog-mailx.py example.com -e google
```
or  
```bash
python goog-mailx.py example.com -e bing
```

#### Save Results as CSV
```bash
python goog-mailx.py example.com -t csv > emails.csv
```

#### Fetch More Pages for Better Results
```bash
python goog-mailx.py example.com --max-pages 5
```

#### Enable Debug Mode
```bash
python goog-mailx.py example.com --debug
```

#### Use a Proxy
```bash
python goog-mailx.py example.com --proxy http://127.0.0.1:8080
```

---

## Example Output  
```
admin@example.com
contact@example.com
support@example.com
info@example.com
```

---

## How It Works  
1. Constructs a **search query** (`site:example.com email`) for Google/Bing.  
2. Uses **Selenium** to load search results dynamically.  
3. Extracts **email addresses** using regex patterns.  
4. Outputs the results in **text** or **CSV** format.  

---

## Troubleshooting  

### 1. ChromeDriver Version Mismatch  
If you encounter an error related to ChromeDriver, update it to match your Chrome version:  
```bash
chromedriver --version
```
Download the latest version from [ChromeDriver](https://chromedriver.chromium.org/downloads).

### 2. No Emails Found?  
- Try increasing `--max-pages` to get more results.  
- Use **Google Search** instead of Bing (`-e google`).  
- Run with **--debug** to inspect the fetched HTML content.  

---

## Disclaimer  
This tool is intended for ethical OSINT research and security testing **with proper authorization**. The author is **not responsible** for any misuse.  

---

## Contributions  
Feel free to contribute by opening a **pull request** or reporting issues in the repository. 🚀  

---


