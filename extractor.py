from bs4 import BeautifulSoup as bs

htmlFile = bs(open("NetflixMyListExtract.html", encoding="utf8"), "html.parser")

listFilm = []
for filmName in htmlFile.find_all("div", {"class": "fallback-text"}):
    listFilm.append(filmName.text)
listFilm.sort()
for filmName in listFilm:
    print(filmName)
