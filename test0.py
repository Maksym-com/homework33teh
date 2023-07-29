from bs4 import BeautifulSoup
import requests
import pandas as pd

site_to_parse = "http://yermilovcentre.org/medias/"
my_answer = requests.get(site_to_parse)
soup = BeautifulSoup(my_answer.content, "html.parser")

for data in soup.select("a > div"):
    print(f"{data.text} - {site_to_parse + data.get('href', '')}")
