import requests
from bs4 import BeautifulSoup

def printThePattern(url:str) -> None:
  htmlPart  = requests.get(url).text
  rows = BeautifulSoup(htmlPart,"html.parser").find("table").find_all("tr")[1:]

  points = []
  for r in rows:
    x ,char , y = [col.get_text(strip = True) for col in r.find_all("td") ]
    points.append((int(x) , int(y) , char))
  maxofX = max(p[0] for p in  points)
  maxofY = max(p[1] for p in points)
  grid  = [[" "]* (maxofX + 1) for  _ in range(maxofY+1)]

  for x , y , char in points:
    grid[y][x] = char
  for r in grid:
    print(" ".join(r))

printThePattern("https://example.com")