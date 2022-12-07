from bs4 import BeautifulSoup
import requests
import pandas as pd

def display_output(name, location, price, built_year, floor, bedroom, bathroom, area, distance_to_transport, facilities):
    print(f'''
    Name: {name}
    Location: {location}
    Price: {price}
    Built Year: {built_year}
    Floor: {floor}
    Bedroom: {bedroom}
    Bathroom: {bathroom}
    Area: {area}
    Distance_to_transportation: {distance_to_transport}
    Facilities: {facilities}
    ''')
    print('')

name_list = []
location_list = []
price_list = []
built_year_list = []
floor_list = []
bedroom_list = []
bathroom_list = []
area_list = []
distance_to_transport_list = []
facilities_list = []

def append_list(name, location, price, built_year, floor, bedroom, bathroom, area, distance_to_transport, facilities):
    name_list.append(name)
    location_list.append(location)
    price_list.append(price)
    built_year_list.append(built_year)
    floor_list.append(floor)
    bedroom_list.append(bedroom)
    bathroom_list.append(bathroom)
    area_list.append(area)
    distance_to_transport_list.append(distance_to_transport)
    facilities_list.append(facilities)

count = 0

for i in range(1307):
    if i == 0:
        html_text = requests.get('https://propertyscout.co.th/%E0%B8%82%E0%B8%B2%E0%B8%A2/%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94/').text
    else:
        link = 'https://propertyscout.co.th/%E0%B8%82%E0%B8%B2%E0%B8%A2/%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-' + str(i+1) + '/'
        html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    rooms = soup.find_all('div', class_='min-h-property-card max-md:min-h-property-card-mobile')
    for j, room in enumerate(rooms):
        if room.find('span', class_='Rental_card__icon_detail__train__3vlDm text-primary-darkgray') is not None:
            if i == 0 or (i!=0 and j<=1):
                name = room.find('strong', class_='Rental_card__name__JhnRh').text
                location = room.find('p', class_='Rental_card__address__3H8NF').text
                price = room.find('div', class_='Rental_listing_price__lF63h').text
                bedroom = room.find('div', class_='Rental_card__icon_detail__bed__5jkyh text-primary-darkgray').text
                bathroom = room.find('span', class_="Rental_card__icon_detail__bathroom__2vKGM text-primary-darkgray" ).text
                area = room.find('span', class_='Rental_card__icon_detail__sqm__B4FGR text-primary-darkgray').text
                distance_to_transport = room.find('span', class_='Rental_card__icon_detail__train__3vlDm text-primary-darkgray').text
                a_href = room.find('a', class_='w-full').get('href')
                html_text2 = requests.get(a_href).text
                soup2 = BeautifulSoup(html_text2, 'lxml')
                info = soup2.find('div', class_= 'text-base property-listing-about')
                info_text = soup2.find('div', class_= 'text-base property-listing-about').text
                try:
                    floor = info_text.split(' ')
                    floor = floor[floor.index('ชั้น')+1]
                except:
                    floor = None
                try:
                    built_year = info.find_all('ul', class_='list-features')[0].text
                    info = info.find_all('ul', class_='list-features')[1]
                except:
                    built_year = None
                    try:
                        info = info.find_all('ul', class_='list-features')[0]
                    except:
                        info = None
                if info is not None:
                    strs = str(info).split('</li><li>')
                    str0 = strs[0][30:]
                    str_1 = strs[-1][:-10] 
                    facilities = strs[1:-1]
                    facilities.append(str0)
                    facilities.append(str_1)
                    display_output(name, location, price, built_year, floor, bedroom, bathroom, area, distance_to_transport, facilities)
                    append_list(name, location, price, built_year, floor, bedroom, bathroom, area, distance_to_transport, facilities)
                else:
                    display_output(name, location, price, built_year, floor, bedroom, bathroom, area, distance_to_transport, None)
                    append_list(name, location, price, built_year, floor, bedroom, bathroom, area, distance_to_transport, None)
                count+=1
                print(count)
        else:
            if i == 0 or (i!=0 and j<=1):
                name = room.find('strong', class_='Rental_card__name__JhnRh').text
                location = room.find('p', class_='Rental_card__address__3H8NF').text
                price = room.find('div', class_='Rental_listing_price__lF63h').text
                bedroom = room.find('div', class_='Rental_card__icon_detail__bed__5jkyh text-primary-darkgray').text
                bathroom = room.find('span', class_="Rental_card__icon_detail__bathroom__2vKGM text-primary-darkgray" ).text
                area = room.find('span', class_='Rental_card__icon_detail__sqm__B4FGR text-primary-darkgray').text
                a_href = room.find('a', class_='w-full').get('href')
                html_text2 = requests.get(a_href).text
                soup2 = BeautifulSoup(html_text2, 'lxml')
                info = soup2.find('div', class_= 'text-base property-listing-about')
                info_text = soup2.find('div', class_= 'text-base property-listing-about').text
                try:
                    floor = info_text.split(' ')
                    floor = floor[floor.index('ชั้น')+1]
                except:
                    floor = None
                try:
                    built_year = info.find_all('ul', class_='list-features')[0].text
                    info = info.find_all('ul', class_='list-features')[1]
                except:
                    built_year = None
                    try:
                        info = info.find_all('ul', class_='list-features')[0]
                    except:
                        info = None
                if info is not None:
                    strs = str(info).split('</li><li>')
                    str0 = strs[0][30:]
                    str_1 = strs[-1][:-10] 
                    facilities = strs[1:-1]
                    facilities.append(str0)
                    facilities.append(str_1)
                    display_output(name, location, price, built_year, floor, bedroom, bathroom, area, None, facilities)
                    append_list(name, location, price, built_year, floor, bedroom, bathroom, area, None, facilities)
                else:
                    display_output(name, location, price, built_year, floor, bedroom, bathroom, area, None, None)
                    append_list(name, location, price, built_year, floor, bedroom, bathroom, area, None, None)
                count+=1
                print(count)

df = pd.DataFrame({'name_list': name_list,
                    'location_list': location_list,
                    'price_list': price_list,
                    'built_year_list': built_year_list,
                    'floor_list': floor_list,
                    'bedroom_list': bedroom_list,
                    'bathroom_list': bathroom_list,
                    'area_list': area_list,
                    'distance_to_transport_list': distance_to_transport_list,
                    'facilities_list': facilities_list})

df.to_csv('dataset.csv',index=False)