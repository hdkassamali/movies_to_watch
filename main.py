import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_data = response.text
soup = BeautifulSoup(movie_data, "html.parser")

website_titles = soup.find_all(name="h3", class_="title")

movie_titles = []

for movie in website_titles:
  movie_titles.append(movie.get_text())

movie_titles.reverse()

with open("movies.txt", mode="w") as file:
  for movie in movie_titles:
    file.writelines(f"{movie}\n")