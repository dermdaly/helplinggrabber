from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import hashlib

# Setup download directory
download_dir = os.path.abspath("downloads")
os.makedirs(download_dir, exist_ok=True)

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {
    "download.default_directory": download_dir,
    "plugins.always_open_pdf_externally": True,
    "download.prompt_for_download": False,
}
options.add_experimental_option("prefs", prefs)

# Start browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://app.helpling.ie/customer/invoices")
input("Log in manually, then press Enter here to continue...")

# Wait for invoice container to appear
time.sleep(5)

# Get the scrollable container
scroll_container = driver.find_element(
    By.CSS_SELECTOR,
    "div.css-175oi2r.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-agouwx > div"
)

# Track processed invoice hashes to avoid duplicates
processed = set()
scroll_attempts = 0
max_scroll_attempts = 10

def hash_invoice_element(el):
    try:
        parent = el.find_element(By.XPATH, "./ancestor::div[3]")
        text = parent.text.strip()
        return hashlib.sha1(text.encode()).hexdigest()
    except:
        return None

while scroll_attempts < max_scroll_attempts:
    invoice_elements = driver.find_elements(By.XPATH, "//div[text()='Invoice']")
    new_found = 0

    for el in invoice_elements:
        h = hash_invoice_element(el)
        if h and h not in processed:
            new_found += 1
            processed.add(h)
            print(f"Processing invoice: {h}")
            try:
                driver.execute_script("arguments[0].scrollIntoView();", el)
                time.sleep(1)
                clickable = el.find_element(By.XPATH, "./ancestor::div[2]")
                clickable.click()
                time.sleep(3)
            except Exception as e:
                print(f"Error clicking invoice: {e}")

    print(f"Scrolled. Found and processed {new_found} new invoice(s).")
    
    if new_found == 0:
        scroll_attempts += 1
    else:
        scroll_attempts = 0

    # Scroll down slightly to load more
    driver.execute_script("arguments[0].scrollTop += 500", scroll_container)
    time.sleep(2.5)

print("Finished processing invoices.")
# driver.quit()