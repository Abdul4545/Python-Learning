import requests
from bs4 import BeautifulSoup

url = "https://abdul-moid.netlify.app"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for heading in soup.find_all("h5"):
    print(heading.text)

# print(soup.prettify())