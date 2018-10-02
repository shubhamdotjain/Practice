import datetime, time
import requests, zipfile, StringIO

path = raw_input("Enter path where you want to download files")

for i in range(1,366):
	date = datetime.datetime.fromtimestamp(time.time()) - datetime.timedelta(i)
	if date.weekday() ==6 or date.weekday() ==5:
		print("Skipping date:", date.strftime('%d-%b-%Y,%A'))
		continue
	month= date.strftime('%b')
	month = month.upper()
	year = date.strftime('%Y')
	day = date.strftime('%d')
	url = "https://www.nseindia.com/content/historical/EQUITIES/" + str(year) + "/" + str(month) + "/cm" + str(day) + str(month) + str(year) + "bhav.csv.zip"
	print("Downloading", url)
	r = requests.get(url, stream=True)
	zip_file = zipfile.ZipFile(StringIO.StringIO(r.content))
	try:
		zip_file.extractall()
	except:
		zip_file.extractall()