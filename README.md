# RemoteOK Job Scraper

A Python web scraping project that extracts remote job listings from the RemoteOK API.

## Features

- Extracts:
  - Job title
  - Company
  - Tags
  - Salary
  - Location
  - Date
  - Full description
- Cleans malformed text and encoding issues
- Removes HTML tags from descriptions
- Exports data to CSV
- Uses API-based scraping instead of HTML scraping

## Technologies Used

- Python
- Requests
- Pandas
- BeautifulSoup4
- ftfy

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Output

Scraped jobs are saved to:

```bash
jobs.csv
```

## Preview

![Preview](preview.png)

## Notes

This project uses the RemoteOK public API for educational purposes.