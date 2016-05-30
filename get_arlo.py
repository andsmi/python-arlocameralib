import keyring
import time
import urllib2
import urllib
import json
username = keyring.get_password("arlo","username")
password = keyring.get_password("arlo","password")

payload= '{"email" :"' + username + '","password":"' + password + '"}'
url = 'https://arlo.netgear.com/hmsweb/login'

while(1):
	req  = urllib2.Request(url,payload, {'Content-Type': 'application/json'})
	page = urllib2.urlopen(req)
	response = json.load(page)
	token = response["data"]["token"]
	auth = response["data"]["authenticated"]
	urlforDevices = 'https://arlo.netgear.com/hmsweb/users/devices?t=' +   `auth`
	authHeaders = {'Content-Type': 'application/json','Authorization':token}
	req  = urllib2.Request(urlforDevices, headers=authHeaders)
	page = urllib2.urlopen(req)
	print urlforDevices
	devices = json.load(page)
	i=0
	for d in devices["data"]:
		print d["deviceName"] + "  " + d["deviceType"]
		if d["deviceType"]=="camera" :
			page = urllib2.urlopen(req)
			newdevices = json.load(page)["data"]
		 	presignedLastImageUrl = newdevices[i]["presignedLastImageUrl"]	
		#	print presignedLastImageUrl
			print time.strftime("Snapshot taken " + d["deviceName"] + " %Y-%m-%d  %H:%M:%S")
		 	#presignedFullFrameSnapshotUrl = newdevices[i]["presignedFullFrameSnapshotUrl"]	
			#urllib.urlretrieve(presignedFullFrameSnapshotUrl, "local-filename.jpg")
			urllib.urlretrieve(presignedLastImageUrl, time.strftime(d["deviceName"] + "_%Y%m%d-%H%M%S.jpg"))
		i += 1
	time.sleep(600)



#soup = BeautifulSoup(page.read())
#print soup
