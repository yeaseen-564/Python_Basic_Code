import requests
import re

url = "https://books.toscrape.com/"  # Books to Scrape url

res = requests.get(url)  # res variable and sent request of the url
text = res.text  # request accepted
text = re.sub("\s+", " ", text)  # Substitute of more than one space

# Finding the book link from the source code:
half_book_link = re.findall('<article class="product_pod">\s*.*?\s*<a href="(.+?)">', text)

# Extracting the half_book_link into full_book_link:
full_book_link = ["https://books.toscrape.com/" + x for x in half_book_link]

# Finding all the name of the books:
all_book_name = re.findall('<article class="product_pod">\s*.*?\s*<a href=".+?">\s*.*?alt="[It&#39;s]*\s*(.+?)"', text)

# print(all_book_name)
# print(full_book_link)

for book in all_book_name:  # printing elements line by line from the li:
    print("Book Name: ", book)
print("")
print("")
for link in full_book_link:
    print("Book Link: ", link)

