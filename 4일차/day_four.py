import requests
import os

print("Welcome to IsItDown.py!")
print("Please write a URL or URLS you want to check. (separated by comma)")
SPLIT = []
URL = []
RESTART = "https://replit.com/@take34362/Day-Four-Blueprint-2#main.py"

SPLIT = input().split(',')

for x in SPLIT:
    if x != x.startswith('http://'):
        http = "http://"
        URL.append(http + x.lower().strip())

try:
    for url in URL:
        r = requests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            print(url + " is up!")
except Exception:
    if url.endswith(".com" and "co.kr" and "go.kr"):
        print(url + "  is down!")
    else:
        print(url + " is not a valid answer")
finally:
    restart = input("Do you want to restart over? y/n")
    if restart == str("y"):
        os.system("clear")
        os.system("python main.py")
    else:
        print("bye")
