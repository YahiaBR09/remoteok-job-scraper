import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 5):

    url = base_url.format(page)

    print(f"Scraping page {page}...")

    try:
        response = requests.get(url, timeout=10)

    except requests.exceptions.RequestException as e:
        print(f"Error on page {page}: {e}")
        continue

    time.sleep(1)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]
        
        title_link = book.h3.a["href"]

        price = book.find(
            "p",
            class_="price_color"
        ).text.replace("Â", "")
        price = price.replace("£", "")
        price = float(price)

        image_url = "https://books.toscrape.com/" + book.find("img")["src"].replace("../", "")

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        book_url = "https://books.toscrape.com/catalogue/" + title_link
        try:
            book_response = requests.get(book_url, timeout=10)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching book details for '{title}': {e}")
            continue

        time.sleep(1)
        
        book_soup = BeautifulSoup(book_response.text, "html.parser")
        description_tag = book_soup.find("div", id="product_description")
        description = description_tag.find_next_sibling("p").get_text(" ", strip=True) if description_tag else "No description available."

        half = len(description) // 2

        if description[:half] == description[half:]:
            description = description[:half]

        upc = book_soup.find("th", string="UPC").find_next_sibling("td").text

        stock = book_soup.find("th", string="Availability").find_next_sibling("td").text.strip()
        stock = stock.replace("In stock (", "").replace(" available)", "")

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Image URL": image_url,
            "Description": description,
            "UPC": upc,
            "Stock": stock
        })


df = pd.DataFrame(all_books)

df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print("Saved books.csv successfully!")