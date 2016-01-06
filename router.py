import BaseHTTPServer

import requests
from flickr_search import get_location_images

from urlparse import urlsplit, parse_qs, urlparse
import cgi

from db_master import insert_favorites, get_favorites

class Handler( BaseHTTPServer.BaseHTTPRequestHandler ):
	def do_GET( self ):

		response = ''
		parsed_path = urlparse(self.path)

		self.send_response(200)
		self.send_header( 'Content-type', 'text/html' )
		self.end_headers()

		options = 	{
					'/' :home,
					'/get_location_images': get_location_img, 		 	# 1 GET
					'/get_next10':get_next10,							# 2 GET
				# 	'/get_images_by_latlong':get_images_by_latlong,		# 3 GET
				# 	'/get_favs':get_favs,								# 6 GET 
				 	'/app.js':appjs,
				 	'/get_fav':get_fav,
				}


		print 'path',parsed_path.path
		print  '/get_next10' == parsed_path.path
				
	


		if parsed_path.path in options:
			for route in options:
				if route == parsed_path.path:
					if 'location' in parsed_path.query:
				
						params= parse_qs(parsed_path.query, keep_blank_values=True)

						response=get_location_img(location=params['location'][0])
						return self.wfile.write(response)

					response=options[route]()

				elif '/get_next10' == parsed_path.path:
						params= parse_qs(parsed_path.query, keep_blank_values=True)
						print parsed_path.query
						print parsed_path.path
						print "Getting 10"
						response = get_next10(location=params['location'][0],page=params['page'][0])
						
						return self.wfile.write(response)
					
					
				
				
					

		return self.wfile.write(response)


	def do_POST( self ):

		response = None
		parsed_path = urlparse(self.path)
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

		options = 	{

					# '/save_latlong': save_latlong,				# 4 POST params locations name
					'/add_to_fav':add_to_fav,						# 5 POST parmas img id
				}

		
		if parsed_path.path in options:
			for route in options:
				if 'add_to_fav' in parsed_path.path:

					if ctype == 'application/x-www-form-urlencoded':
						length = int(self.headers.getheader('content-length'))
						postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
						add_to_fav(img=postvars['image'][0])
						self.send_response(302)
						self.send_header("Location",'/')
						self.end_headers()



		

		return self.wfile.write(response)


def home():
	return open('index.html','r').read()

		
def appjs():
	return open('app.js','r').read()


def get_location_img(location):
	
	temp = get_location_images(location)

	return  temp

def get_next10(location,page):
	print location
	print page
	print "getting 10"
	temp=get_location_images(location,page)
	return temp

def add_to_fav(img):
	# write to db
	
	insert_favorites(img)
	
	

def get_fav():
	
	res= get_favorites()
	
	return res
	


def save_latlong(lat,lon):
	# write to db
	pass

httpd = BaseHTTPServer.HTTPServer( ('127.0.0.1', 8080), Handler )
httpd.serve_forever()