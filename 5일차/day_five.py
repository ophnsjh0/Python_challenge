import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"


def extract_code(html):
    country = html.find("td")
    if country is not None:
        country = str(country.get_text())
    else:
        country = ''

    return text


def extract_iban_pages():
    codes = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table", {"class": "table"})
    results = table.find_all("tr")
    for result in results:
        code = extract_code(result)
        codes.append(code)
        print(code)

    return codes


extrct_iban = extract_iban_pages()

print(extrct_iban)
