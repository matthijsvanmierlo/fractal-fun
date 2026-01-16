
from playwright.sync_api import sync_playwright
import os

def run():
    # Get the absolute path to index.html
    cwd = os.getcwd()
    file_url = f'file://{cwd}/index.html'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Adjust viewport to standard HD
        page.set_viewport_size({'width': 1280, 'height': 720})

        print(f'Navigating to {file_url}')
        page.goto(file_url)

        # Wait for the canvas to be present
        page.wait_for_selector('canvas')

        # Test UI Elements: Check if reset button and export frame toggle exist
        reset_btn = page.get_by_title('Reset View')
        export_chk = page.get_by_label('Show Export Frame (16:9)')
        # Note: get_by_label looks for associated label. My checkbox has text next to it but maybe not explicitly 'for' linked in a standard way playwright likes?
        # My HTML: <input type='checkbox' id='check-export-frame'> <span ...>Show Export Frame...</span>
        # So I should use locator for id

        # Take initial screenshot
        page.screenshot(path='verification/initial.png')
        print('Initial screenshot taken')

        # Enable Export Frame
        page.check('#check-export-frame')
        page.wait_for_selector('#export-frame') # Should be visible now

        # Take screenshot with export frame
        page.screenshot(path='verification/export_frame.png')
        print('Export frame screenshot taken')

        # Interact with Reset
        page.click('#btn-reset')

        browser.close()

if __name__ == '__main__':
    run()
