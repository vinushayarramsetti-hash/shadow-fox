import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    # Create CSV file
    with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:

        writer = csv.writer(file)

        # CSV headings
        writer.writerow([
            "Title",
            "Price",
            "Availability",
            "Rating"
        ])

        # Extract book information
        for book in books:

            title = book.h3.a["title"]

            price = book.find(
                "p",
                class_="price_color"
            ).text

            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()

            rating = book.find("p")["class"][1]

            # Write data into CSV
            writer.writerow([
                title,
                price,
                availability,
                rating
            ])

    print("Data successfully saved to books.csv")

else:
    print("Website could not be accessed")