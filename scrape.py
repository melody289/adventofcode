import requests

URL = "https://adventofcode.com/2021/day/1/input"
page = requests.get(URL)

print(page.text)