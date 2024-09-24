import requests
import re

base_url = "https://quera.org/blog/"


def get_latest_post():
    r = requests.get('https://quera.org/blog/')
    print(re.findall(r'<h4> <a href="(.*)">(.*)</a></h4>', r.text))

