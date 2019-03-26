import sys
import mechanize as mech
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print("ARGS:",str(sys.argv))
br = mech.Browser()
br.set_handle_robots(False)   # ignore robots
res = br.open('http://www.fourmilab.ch/cgi-bin/Yoursky')

link = br.find_link("Customise")
br.follow_link(link)
print("URL:",br.geturl())


#Selects the form we want
br.form = list(br.forms())[0]


#Set dynimg so we just get an image instd of a map
control = br.form.find_control("dynimg")
control.items[0].selected=True

#Set lat and lon values
control = br.form.find_control("lat")
control.value = sys.argv[1]

control = br.form.find_control("lon")
control.value = sys.argv[2]

#submit form
res = br.submit()

#download generate img
img = open('sky.jpg','wb')
img.write(requests.get(br.geturl()).content)
img.close()

#display image
img = mpimg.imread('sky.jpg')
imgplot = plt.imshow(img)
plt.show()