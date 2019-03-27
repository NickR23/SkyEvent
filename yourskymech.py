from spinner import Spinner
import sys
import mechanize as mech
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

spinner = Spinner() #Make spinner
spinner.start()

argc = len(sys.argv)
br = mech.Browser()
br.set_handle_robots(False)   # ignore robots
res = br.open('http://www.fourmilab.ch/cgi-bin/Yoursky')

link = br.find_link("Customise")
br.follow_link(link)
#print("URL:",br.geturl())
spinner.stop()
print(argc,"ARGS:",str(sys.argv))

#Selects the form we want
br.form = list(br.forms())[0]


  
#Set dynimg so we just get an image instd of a map
control = br.form.find_control("dynimg")
control.items[0].selected=True
#Set color scheme
control = br.form.find_control("scheme")
control.value=["3"]
#Disable star names
br.form.find_control("starn").items[0].selected=False
#Disable boundaries
br.form.find_control("constb").items[0].selected=False
#Disable names
br.form.find_control("constn").items[0].selected=False
#Disable coords
br.form.find_control("coords").items[0].selected=False

#Set lat and lon values
lat = '0'
lon = '0'
if argc > 1:
  lon = argv[1]
if argc > 2:
  lat = argv[2]
control = br.form.find_control("lat")
control.value = lat

control = br.form.find_control("lon")
control.value = lon

#for c in br.form.controls:
  #print(c)
#submit form
res = br.submit()

#download generate img
img = open('sky.jpg','wb')
img.write(requests.get(br.geturl()).content)
img.close()

#Show cool moon dude
f = open('assets/title.txt', 'r')
moon_dude = f.read()
print(moon_dude)
f.close()

#display image
img = Image.open('sky.jpg')
img.show()