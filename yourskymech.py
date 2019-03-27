from spinner import Spinner
import form_filler as filler
import sys
import mechanize as mech
import requests
from PIL import Image

spinner = Spinner() #Make spinner
spinner.start()

br = mech.Browser()
br.set_handle_robots(False)   # ignore robots
res = br.open('http://www.fourmilab.ch/cgi-bin/Yoursky')

link = br.find_link("Customise")
br.follow_link(link)
spinner.stop()

#Fill out form
filler.fill_form( br, sys.argv )

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