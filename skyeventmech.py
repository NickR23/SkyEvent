from spinner import Spinner
import form_filler as filler
import mechanize as mech
import requests
from PIL import Image
import urllib.request

def get_moon_dude():
	f = open('assets/title.txt', 'r')
	moon_dude = f.read()
	f.close()
	return moon_dude


def main_process(argv):
	spinner = Spinner() #Make spinner
	spinner.start()
	print('argv:',argv)

	br = mech.Browser()
	br.set_handle_robots(False)   # ignore robots
	res = br.open('http://www.fourmilab.ch/cgi-bin/Yoursky')

	link = br.find_link("Customise")
	br.follow_link(link)
	  
	spinner.stop()

	#Fill out form
	filler.fill_form(br,argv)

	#submit form
	res = br.submit()

	#download generate img
	img=open('pic/sky.jpg','wb')
	img.write(requests.get(br.geturl()).content)
	img.close()

	#Show cool moon dude
	moon_dude = get_moon_dude()
	print(moon_dude)
	#display image
	img = Image.open('pic/sky.jpg')
	img.show()