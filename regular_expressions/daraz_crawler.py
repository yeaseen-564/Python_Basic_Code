import requests
import re

url = "https://www.daraz.com.bd"

res = requests.get(url)
text = res.text
text = re.sub("\s+", " ", text)

item_finder = re.findall('<a class="drz-footer-category-tag" href="(.*?)"', text)
links = ["https:" + x for x in item_finder]
for link in links:
    print("Category Link:", link)


