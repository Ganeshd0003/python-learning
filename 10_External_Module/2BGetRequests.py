# get the html code of the given site and save it in html file via file handling

import requests

r = requests.get("https://www.google.com")

with open("2bindex.html","w+") as f:
    f.write(r.text)