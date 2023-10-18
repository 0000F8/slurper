from decouple import config
import psycopg2

import requests
from bs4 import BeautifulSoup
import sys
import asyncio
from pyppeteer import launch

# Load database settings from the .env file
DATABASE_NAME = config('DATABASE_NAME')
DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST')
DATABASE_PORT = config('DATABASE_PORT')

# Function to connect to the PostgreSQL database and retrieve a site URL
def get_site_url_from_db():
    connection = psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    cursor = connection.cursor()
    cursor.execute("SELECT site_url FROM sites LIMIT 1")
    site_url = cursor.fetchone()[0]  # Assuming one site URL is retrieved
    connection.close()
    return site_url

# Function to visit a site and extract all text
def extract_text_from_site(site_url):
    response = requests.get(site_url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        return text
    else:
        return None

async def capture_full_page_screenshot(url, output_path):
    browser = await launch(headless=True)  # Launch a headless Chromium browser
    page = await browser.newPage()

    # Navigate to the URL
    await page.goto(url)

    # Get the full content height of the page
    bodyHandle = await page.J('body')
    height = await page.evaluate('(element) => element.scrollHeight', bodyHandle)

    # Set the viewport size to match the full page height
    await page.setViewport({'width': 1200, 'height': height})

    # Capture the full-page screenshot
    await page.screenshot({'path': output_path, 'fullPage': True})

    # Close the browser
    await browser.close()

async def main():
    if len(sys.argv) > 1:
        site_url = sys.argv[1]  # Use the argument as the site URL
    else:
        # If no argument is provided, retrieve the site URL from the database
        site_url = get_site_url_from_db()

    if site_url:
        extracted_text = extract_text_from_site(site_url)
        if extracted_text:
            print(extracted_text)
        else:
            print("Failed to extract text from the site.")

        # Capture a full-page screenshot after extracting text
        await capture_full_page_screenshot(site_url, "full_page_screenshot.png")
        print("Full-page screenshot saved as full_page_screenshot.png")
    else:
        print("No site URL retrieved from the database.")

if __name__ == "__main__":
    asyncio.run(main())