from bs4 import BeautifulSoup as bs

htmlFile = bs(open("NetflixMyListExtract.html"), "html.parser")

for filmName in htmlFile.find_all("div", {"class": "fallback-text"}):
    print(filmName.text)
