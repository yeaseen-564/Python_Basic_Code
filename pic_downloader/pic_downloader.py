import sys
import requests

url = sys.argv[1]
file_name = sys.argv[2]
response = requests.get(url)
with open(f"{file_name}", "wb") as f:
    f.write(response.content)
