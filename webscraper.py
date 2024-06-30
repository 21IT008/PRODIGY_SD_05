import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website
url = 'http://books.toscrape.com/'

# Send an HTTP request to the website
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract book information
book_titles = []
book_prices = []
book_ratings = []

for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.find('p', class_='star-rating')['class'][1]  # Get the second class name
    # rating = rating_dict.get(rating_class, 0)  # Convert to numeric rating
    
    book_titles.append(title)
    book_prices.append(price)
    book_ratings.append(rating)

# Create a DataFrame
data = {
    'Book Title': book_titles,
    'Price': book_prices,
    'Rating': book_ratings
}
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('books.csv', index=True)

print('Book information has been successfully scraped and saved to books.csv')
