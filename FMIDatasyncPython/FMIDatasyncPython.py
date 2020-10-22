import urllib.request
import urllib.parse
import getopt, sys
#This script will send http request to Azure Function,
#Azure Function will then fetch specific file from S3 and store it to Azure Storage
#Path variable is S3 file path without main container, example ko/fmimeteo/observations/2020-09.csv
#Datetime is S3 Last modified time in ISO 8601 format, example 2020-10-01T00:00:09.0000000Z
#Delete parameter is used to delete file, delete must be delete, if something else it will download/update it. usage example delete=delete
print("Send request...");
# Get full command-line arguments
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
print(argument_list)
short_options = "ptd"
long_options = ["path=","datetime=","delete="]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)
filepath = ""
datetime = ""
delete = False
for current_argument, current_value in arguments:
	if current_argument in ("-p", "--path"):
		filepath = current_value
		print("path : " + current_value)
	elif current_argument in ("-t", "--datetime"):
		datetime=current_value
		print("datetime : " + current_value)
	elif current_argument in ("-d", "--delete"):
		if current_value == "delete":
			delete = True
		print("delete: " + current_value)

def updatefile(filepath,datetime):
	url = 'https://datasyncfmihamk.azurewebsites.net/api/Function1?code=ymzW2KlRgurzmNzOB3ReHhWrVxLJhHj7mhQHou3THRcrKxAXSujnkg==&filepath=' + filepath + '&datetime=' + datetime
	print('opening URL: ')
	print(url)
	getUrl(url)
	return
def deletefile(filepath,datetime):
	url = 'https://datasyncfmihamk.azurewebsites.net/api/Function1?code=ymzW2KlRgurzmNzOB3ReHhWrVxLJhHj7mhQHou3THRcrKxAXSujnkg==&filepath=' + filepath + '&deletefile=true' + '&datetime=' + datetime
	print('DELETING URL:')
	print(url)
	getUrl(url)
	return
def log(item, url):
	print(item)
	print(url)

def getUrl(url):
	try:
		with urllib.request.urlopen(url) as response:
			log(response.code, url)
			print(response.read())
	except urllib.error.HTTPError  as e:
		log(e.code, url)
		print(e.read())
	except urllib.error.URLError as e:
		if hasattr(e, 'reason'):
			log(e.reason, url)
		elif hasattr(e, 'code'):
			log(e.code, url)
print(f"delete= {delete}");
if delete == False:
	updatefile(filepath,datetime)
if delete == True:
	deletefile(filepath,datetime)


