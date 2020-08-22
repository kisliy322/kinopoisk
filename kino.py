from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests
main_link = 'https://www.kinopoisk.ru'
response = requests.get(main_link + '/afisha/new/city/1/').text
html = bs(response,'lxml')

films_block = html.find('div',{'class':'filmsListNew'})

films_list = films_block.findChildren(recursive=False)

films=[]

for film in films_list:
	film_data = {}
	main_info = film.find('div',{'class':'name'}).findChild()
	film_name = main_info.getText()
	film_link = main_link + main_info['href']
	genre = film.findAll('div',{'class':'gray'})[1].getText().replace(' ','')[9:]
	rating = film.find('span',{'class':['rating_ball_grey','rating_ball_green','rating_ball_red']})
	if not rating:
		rating = 0
	else:
		rating = float(rating.getText())

	film_data['name'] = film_name
	film_data['genre'] = genre
	film_data['link'] = film_link
	film_data['rating'] = rating
	films.append(film_data)

pprint(films)