import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

website_titles = soup.find_all(name="h3", class_="title")

movie_titles = [movie.get_text() for movie in website_titles]

new_movie_list = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
  for movie in new_movie_list:
    file.write(f"{movie}\n")