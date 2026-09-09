# get the html code of the given site and print it

import requests

r = requests.get("https://www.google.com")

print(r.text)