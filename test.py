from bs4 import BeautifulSoup
import requests

#link = 'https://propertyscout.co.th/%E0%B8%82%E0%B8%B2%E0%B8%A2/%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-' + '2' + '/'
#html_text = requests.get(link).text
#soup = BeautifulSoup(html_text, 'lxml')
html_text = requests.get('https://propertyscout.co.th/%E0%B8%82%E0%B8%B2%E0%B8%A2/%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-2/').text
#print(requests.get('https://propertyscout.co.th/%E0%B8%82%E0%B8%B2%E0%B8%A2/%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94/2'))
soup = BeautifulSoup(html_text, 'lxml')
rooms = soup.find_all('div', class_='Rental_card__content__BV1iK bg-secondary-darkwhite')
for room in rooms:
    print(room.text)