# Books To Scrape Web Scraper

A Python web scraping project that extracts book data from BooksToScrape.com using Requests and BeautifulSoup.

## Preview

![Preview](preview.png)

## Features

- Scrapes multiple pages automatically
- Extracts:
  - Title
  - Price
  - Rating
  - Image URL
  - Description
  - UPC
  - Stock availability
- Handles request errors
- Saves data to CSV

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Output

The scraped data is saved to:

```bash
books.csv
```