import requests,bs4,os
os.makedirs('C:/Users/sunil/Desktop/Python/Workspace/comic')
url='http://xkcd.com'
while not url.endswith('#'):
#url donwload	
	res=requests.get(url)
	res.raise_for_status()
#download comic image

	soup=bs4.BeautifulSoup(res.text,'html.parser')
	ans=soup.select('#comic img')
	if ans==[]:
		print('Images not found')
	else:
		try:
			image_url='https:'+ans[0].get('src')
			res=requests.get(image_url)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			prev_url=soup.select('a[rel="prev"]')[0]
			url='http://xkcd.com' + prev_url.get('href')
#save the image
	file_location='C:/Users/sunil/Desktop/Python/Workspace/comic/'+image_url.split('/')[-1       ]
	image_file=open(file_location,'wb')
	for chunk in res.iter_content(100000):
		image_file.write(chunk)
	image_file.close()
#prevlink
	prev_url=soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_url.get('href')


