# if we want the data in key value pairs

import requests

r = requests.post("https://www.google.com",data={'key': 'value'})

with open("post.html", "w") as f:
    f.write(r.text)
    