#lets try to hit an api and generate a file based on the info

import requests
#hit my own github
github= requests.get("https://api.github.com/users/po1sigala/repos")

print(github.text)