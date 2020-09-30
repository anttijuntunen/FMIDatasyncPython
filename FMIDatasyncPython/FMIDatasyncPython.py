import urllib.request
import urllib.parse

def updatefile(filepath,datetime):
	url = 'https://datasyncfmihamk.azurewebsites.net/api/Function1?code=ymzW2KlRgurzmNzOB3ReHhWrVxLJhHj7mhQHou3THRcrKxAXSujnkg==&filepath=' + filepath + '&datetime=' + datetime
	print('opening URL:')
	print(url)
	getUrl(url)
	return
def deletefile(filepath):
	url = 'https://datasyncfmihamk.azurewebsites.net/api/Function1?code=ymzW2KlRgurzmNzOB3ReHhWrVxLJhHj7mhQHou3THRcrKxAXSujnkg==&filepath=' + filepath + '&deletefile=true'
	print('DELETING URL:')
	print(url)
	getUrl(url)
	return
def log(item, url):
     print(item)

def getUrl(url):
	try:
		with urllib.request.urlopen(url) as response:
			log(response.code, url,response.read().decode('utf-8'))
	except urllib.error.HTTPError  as e:
		log(e.code, url)
	except urllib.error.URLError as e:
		if hasattr(e, 'reason'):
			log(e.reason, url)
		elif hasattr(e, 'code'):
			log(e.code, url)

filepath = 'ko/fmimeteo/observations/2020-09.csv'
datetime = '2020-09-25T08:42:26'
print(filepath)
print(datetime)
updatefile(filepath,datetime)
#deletefile(filepath)

