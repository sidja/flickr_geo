import requests
from pprint import pprint
import json

from get_image import get_img, get_img_async



'''
https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=85971227c8f4768af7e2e1df89e2d14c&lat=-33.917714&lon=151.234699&format=json&nojsoncallback=1&api_sig=4ce85b55d0cd698d21d2794c32d709d5
'''


def get_lat_lon(location):
	

	payload = 	{
					'q': location, 
					'format': 'json',
					'addressdetails':'1'
				}

	r = requests.get('http://nominatim.openstreetmap.org/search?',params=payload)

	# print r.status_code

	#pprint(r.json())

	lat = r.json()[0]['lat']
	lon = r.json()[0]['lon']

	return lat,lon





def get_lat_lng_images(lat,lon,page):

	payload = 	{
					'method': 'flickr.photos.search', 
					'api_key': '3a9b1899d4f14e6691754be830c8fb66',
					'lat': lat,
					'lon': lon,
					'format': 'json',
					'nojsoncallback':'1',
					'per_page':'10',
					'page':page,
				}

	r = requests.get('https://api.flickr.com/services/rest/',params=payload)

	print r.status_code

	img_list = []

	for p in r.json()['photos']['photo']:
		
		img_list.append(p['id'])

	
	return get_img_async(img_list)





#pprint(get_lat_lng_images(lat = '-33.917714', lon = '151.234699'))



def get_location_images(location,page=1):

	lat,lon = get_lat_lon(location)

	img_list= get_lat_lng_images(lat,lon,page)

	return json.dumps(img_list)


# pprint(get_location_images(location='MCG Melbourne'))
