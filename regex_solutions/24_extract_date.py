import re


# 24) Write a Python program to extract year, month and date from a an url.
def extract_date(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)


url1 = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))
