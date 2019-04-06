from tkinter import *
from tkinter import ttk
from datetime import datetime
import geocoder
import skyeventmech as sem

def get_current_date_string():
	now = datetime.now()
	date = "%d-%02d-%02d %02d:%02d:%02d"%(now.year, now.month, now.day, now.hour, now.minute, now.second)
	return date
def get_location():
	g = geocoder.ip('me')
	return g.latlng

class SkyEvent:
	def __init__(self,master):
		mainframe = Frame(master,padx=10,pady=10)
		mainframe.pack()

		date_and_location_frame=Frame(mainframe,padx=5,pady=5)
		date_and_time = LabelFrame(date_and_location_frame, text='Date and Time', padx=5,pady=5)
		date_and_time.pack(fill=BOTH,side=LEFT)
		location_frame = LabelFrame(date_and_location_frame, text='Location', padx=5,pady=5)
		location_frame.pack(fill=BOTH,side=LEFT)
		date_and_location_frame.pack(anchor=W)

		image_format = LabelFrame(mainframe, text='Image Format', padx=5, pady=5)
		image_format.pack()

		#Date and Time
		self.date_entry=Entry(date_and_time)
		current_date=get_current_date_string()
		self.date_entry.insert(0,current_date)
		now_button=Button(date_and_time, text='Set to current time and date',command=self.set_current_date)
		now_button.pack(anchor=W)
		self.date_entry.pack(anchor=W)

		#Location
		current_location=get_location()
		here_button=Button(location_frame,text='Set to current location',command=self.set_current_location)
		here_button.pack(anchor=W)
		latitude_frame=Frame(location_frame)
		latitude_frame.pack(anchor=W)
		Label(latitude_frame,text='Latitude').pack(side=LEFT)
		self.latitude_entry=Entry(latitude_frame,width=8)
		self.latitude_entry.insert(0,current_location[0])
		self.latitude_entry.pack(side=LEFT)
		self.lat_dir=StringVar()
		self.lat_dir.set("N")
		latitude_radioN=Radiobutton(latitude_frame, text='North', variable=self.lat_dir, value='N').pack(side=LEFT)
		latitude_radioS=Radiobutton(latitude_frame, text='South', variable=self.lat_dir, value='S').pack(side=LEFT)

		longitude_frame=Frame(location_frame)
		longitude_frame.pack(anchor=W)
		Label(longitude_frame,text='Longitude').pack(side=LEFT)
		self.longitude_entry=Entry(longitude_frame,width=8)
		self.longitude_entry.insert(0,current_location[1] * -1)
		self.longitude_entry.pack(side=LEFT)
		self.lon_dir=StringVar()
		self.lon_dir.set("E")
		longitude_radioE=Radiobutton(longitude_frame, text='East', variable=self.lon_dir, value='E').pack(side=LEFT)
		longitude_radioW=Radiobutton(longitude_frame, text='West', variable=self.lon_dir, value='W').pack(side=LEFT)

		#Display
		self.equator_check_val = IntVar()
		equator_check=Checkbutton(image_format, text='Show equator', variable=self.equator_check_val)
		equator_check.pack(anchor=W)

		self.moon_and_planets_check_val = IntVar()
		moon_and_planet_check=Checkbutton(image_format, text='Show moon and planets', variable=self.moon_and_planets_check_val)
		moon_and_planet_check.pack(anchor=W)

		deep_frame=Frame(image_format)
		self.deep_sky_check_val=IntVar()
		deep_sky_check=Checkbutton(deep_frame,text='Show deep sky objects of magnitude',variable=self.deep_sky_check_val)
		deep_sky_check.pack(side=LEFT)
		# deep_sky_frame=Check_label(deep_frame,str="Show deep sky objects of magnitude")
		# self.deep_sky_frame.frame.pack(side=LEFT)
		self.deep_sky_entry=Entry(deep_frame,width=3)
		self.deep_sky_entry.insert(0,'2.5')
		self.deep_sky_entry.pack(side=LEFT)
		Label(deep_frame,text='and brighter').pack(side=LEFT)
		deep_frame.pack(anchor=W)

		#Constellations
		constellations_frame=LabelFrame(image_format, text='Constellations')
		self.outline_check_val=IntVar()
		outlines_check=Checkbutton(constellations_frame,text='Show outlines',variable=self.outline_check_val)
		outlines_check.pack(anchor=W)

		constellations_name_options=Frame(constellations_frame)
		constellations_name_options.pack(anchor=W)
		self.name_check_val=IntVar()
		name_check=Checkbutton(constellations_name_options,text='Show names',variable=self.name_check_val)
		name_check.pack(side=LEFT)
		self.horizon_check_val=IntVar()
		align_horizon_check=Checkbutton(constellations_name_options,text='align name with horizon?',variable=self.horizon_check_val)
		align_horizon_check.pack(side=LEFT)
		self.abbreviate_check_val=IntVar()
		abbreviate_check=Checkbutton(constellations_name_options,text='abbreviate?',variable=self.abbreviate_check_val)
		abbreviate_check.pack(side=LEFT)
		self.boundaries_check_val=IntVar()
		boundaries_check=Checkbutton(constellations_frame,text='Show constellation boundaries',variable=self.boundaries_check_val)
		boundaries_check.pack(anchor=W)
		constellations_frame.pack()

		#Stars
		stars_frame=(LabelFrame(image_format, text='Stars'))

		stars_mag_frame=Frame(stars_frame)
		Label(stars_mag_frame,text='Show stars brighter than magnitude').pack(side=LEFT)
		self.stars_magnitude=Entry(stars_mag_frame,width=3)
		self.stars_magnitude.pack(side=LEFT)
		stars_mag_frame.pack(anchor=W)

		stars_mag_check_frame=Frame(stars_frame)
		self.names_for_mag_check_val=IntVar()
		names_for_mag_check=Checkbutton(stars_mag_check_frame,text='Names for magnitude',variable=self.names_for_mag_check_val)
		names_for_mag_check.pack(side=LEFT)
		self.mag_check_entry=Entry(stars_mag_check_frame,width=3)
		self.mag_check_entry.pack(side=LEFT)
		Label(stars_mag_check_frame,text='and brighter').pack(side=LEFT)
		stars_mag_check_frame.pack(anchor=W)

		stars_bayer_frame=Frame(stars_frame)
		self.bayer_check_val=IntVar()
		bayer_check=Checkbutton(stars_bayer_frame,text='Bayer/Flamsteed codes for magnitude',variable=self.bayer_check_val)
		bayer_check.pack(side=LEFT)
		self.bayer_entry=Entry(stars_bayer_frame,width=3)
		self.bayer_entry.pack(side=LEFT)
		bayer_append=Label(stars_bayer_frame,text='and brighter')
		bayer_append.pack(side=LEFT)
		stars_bayer_frame.pack(anchor=W)

		self.invert_check_val=IntVar()
		invert_check=Checkbutton(stars_frame,text='Invert North and South',variable=self.invert_check_val)
		invert_check.pack(anchor=W)

		image_size_frame=Frame(stars_frame)
		Label(image_size_frame,text='Image size:').pack(side=LEFT)
		self.image_size_entry=Entry(image_size_frame,width=4)
		self.image_size_entry.pack(side=LEFT)
		Label(image_size_frame,text='pixels').pack(side=LEFT)
		image_size_frame.pack(anchor=W)

		font_scale_frame=Frame(stars_frame)
		Label(font_scale_frame,text='Font scale:').pack(side=LEFT)
		self.font_scale_entry=Entry(font_scale_frame,width=3)
		self.font_scale_entry.pack(side=LEFT)
		font_scale_frame.pack(anchor=W)

		color_schemes_frame=Frame(stars_frame)
		Label(color_schemes_frame,text='Color scheme:').pack(side=LEFT)
		self.color_scheme_val=StringVar()
		self.color_scheme_val.set("Color")
		color_options=OptionMenu(color_schemes_frame,self.color_scheme_val,"Color","Black on white","White on black","Night vision (red)")
		color_options.pack(side=LEFT)
		color_schemes_frame.pack(anchor=W)
		stars_frame.pack()


		submit_button=Button(mainframe,text='Submit')
		submit_button.pack()
		img = PhotoImage(file="./assets/happy_moon.png")
		Label(image=img).pack()

		# moon_dude = sem.get_moon_dude()
		# self.title=Label(master,text=moon_dude)
		# self.title.pack()
		# w.pack()
		# field=Entry(master)
		# field.pack()
		master.mainloop()


	def set_current_date(self):
		self.date_entry.delete(0,END)
		self.date_entry.insert(0,get_current_date_string())

	def set_current_location(self):
		current_location=get_location()
		self.latitude_entry.delete(0,END)
		self.latitude_entry.insert(0,current_location[0])
		self.lat_dir.set('N')
		self.longitude_entry.delete(0,END)
		self.longitude_entry.insert(0,current_location[1] * -1)
		self.lon_dir.set('E')
