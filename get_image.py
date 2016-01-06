import requests
from pprint import pprint
from Queue import Queue
from threading import Thread


'''
https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=85971227c8f4768af7e2e1df89e2d14c&lat=-33.917714&lon=151.234699&format=json&nojsoncallback=1&api_sig=4ce85b55d0cd698d21d2794c32d709d5
'''

def get_img(photo_id='23409699606', size='Thumbnail'):
	'''
	Sizes :

			Thumbnail
			Small
			Small 320
			Medium
			Medium 640
			Medium 800
			Large
			Large 1600
			Large 2048
			Original

	'''
	

	payload = 	{
					'method': 'flickr.photos.getSizes', 
					'api_key': '3a9b1899d4f14e6691754be830c8fb66',
					'photo_id':photo_id,
					'format': 'json',
					'nojsoncallback':'1',
					'per_page':'10',
				}

	r = requests.get('https://api.flickr.com/services/rest/',params=payload)

	#print r.status_code

	#pprint(r.json()['sizes']['size'])

	for img in r.json()['sizes']['size']:
		if img['label'] == size :
			return img['source']
	
		#print img['label']


# print get_img()

def get_img_async(pid_list):


	concurrent = 10

	img_list=[]

	def doWork():
	    while True:
	        p_id = q.get()
	        
	        temp = get_img(photo_id=p_id)
	        img_list.append(temp)
	        q.task_done()

	q = Queue(concurrent)
	for i in range(concurrent):
	    t = Thread(target=doWork)
	    t.daemon = True
	    t.start()

	try:
		for i in pid_list:
			# print i
			q.put(i)
		q.join()

	except KeyboardInterrupt:
	    sys.exit(1)


	#print img_list
	return img_list