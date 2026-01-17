
from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Open the local file directly using absolute path inside sandbox
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Wait for initialization
        time.sleep(2)

        # Check if canvas exists
        if page.locator("canvas").count() > 0:
            print("Canvas found")
        else:
            print("Canvas NOT found")

        # Check if Decimal is loaded
        is_decimal_loaded = page.evaluate("typeof Decimal !== \"undefined\"")
        print(f"Decimal loaded: {is_decimal_loaded}")

        # Check if app is initialized
        is_app_initialized = page.evaluate("typeof window.fractalApp !== \"undefined\"")
        print(f"App initialized: {is_app_initialized}")

        # Take screenshot
        page.screenshot(path="verification/screenshot.png")
        browser.close()

if __name__ == "__main__":
    run()
