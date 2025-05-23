# 🏠 Property Web Scraper

A Streamlit-based web application that scrapes property listings from various real estate websites, including Property Onion. The scraper can extract property details like title, price, location, status (available/upcoming/cancelled), and dates.

## Features

- Scrape property listings from Property Onion
- Filter properties by status (Available/Upcoming/Cancelled)
- Export data to CSV format
- Simple and intuitive web interface
- Shows property status distribution with charts

## Prerequisites

- Python 3.8+
- Google Chrome browser installed

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Open the provided URL in your web browser (usually http://localhost:8501)
3. Enter the website URL or use the default Property Onion URL
4. Click "Scrape Properties" to start scraping
5. Once complete, you can view the data and download it as a CSV file

## Supported Websites

- Property Onion (https://propertyonion.com/property_search)
- More websites can be added by extending the scraper functions

## Note

- The scraper uses Selenium with Chrome WebDriver for dynamic content loading
- Make sure you have a stable internet connection
- Some websites might have anti-scraping measures in place

## License

This project is open source and available under the MIT License.
