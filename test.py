from bs4 import BeautifulSoup
import requests
import pandas as pd

site_to_parse = "http://books.toscrape.com"
my_answer = requests.get(site_to_parse)
soup = BeautifulSoup(my_answer.content, "html.parser")

for data in soup.select("h3 > a"):
    print(f"{data.text} - {site_to_parse + data.get('href', '')}")
