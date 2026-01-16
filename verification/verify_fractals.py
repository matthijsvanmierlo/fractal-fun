
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load the index.html file
        # We need to serve it or just load file://
        # Playwright supports file://

        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Wait for the app to initialize
        page.wait_for_selector('canvas')
        page.wait_for_timeout(2000) # Wait for shaders to compile/render

        # Take a screenshot of the initial state (Mandelbrot)
        page.screenshot(path='verification/initial_mandelbrot.png')

        # Change to Julia
        page.select_option('#select-fractal', 'julia')
        page.wait_for_timeout(1000)
        page.screenshot(path='verification/julia.png')

        # Change to Barnsley
        page.select_option('#select-fractal', 'barnsley')
        page.wait_for_timeout(1000)
        page.screenshot(path='verification/barnsley.png')

        browser.close()

if __name__ == '__main__':
    run()
