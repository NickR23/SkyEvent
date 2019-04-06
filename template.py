from tkinter import *
from datetime import datetime
import skyeventmech as sem

def get_current_date_string():
	now = datetime.now()
	date = "%d-%02d-%02d %02d:%02d:%02d"%(now.year, now.month, now.day, now.hour, now.minute, now.second)
	return date


class SkyEvent:
	def __init__(self,master):
		self.mainframe = Frame(master)
		self.mainframe.pack()
		self.date_and_time = LabelFrame(self.mainframe, text='Date and Time', padx=5,pady=5)
		self.date_and_time.pack()

		self.location = LabelFrame(self.mainframe, text='Location', padx=5,pady=5)
		self.location.pack()

		self.image_format = LabelFrame(self.mainframe, text='Image Format', padx=5, pady=5)
		self.image_format.pack()


		self.date_frame=LabelFrame(self.date_and_time, text='Date')
		self.date_frame.pack(anchor=W)
		self.now_check=Checkbutton(self.date_frame, text='Now', onvalue="RGB", offvalue="L")
		self.now_check.pack(anchor=W)
		self.date_entry=Entry(self.date_frame)
		current_date=get_current_date_string()
		self.date_entry.insert(0,current_date)
		self.date_entry.pack(anchor=W)

		self.latitude_frame=Frame(self.location)
		self.latitude_frame.pack()
		self.latitude_label=Label(self.latitude_frame,text='Latitude')
		self.latitude_label.pack(side=LEFT)
		self.latitude_entry=Entry(self.latitude_frame)
		self.latitude_entry.pack(side=LEFT)

		self.longitude_frame=Frame(self.location)
		self.longitude_frame.pack()
		self.longitude_label=Label(self.longitude_frame,text='Longitude')
		self.longitude_label.pack(side=LEFT)
		self.longitude_entry=Entry(self.longitude_frame)
		self.longitude_entry.pack(side=LEFT)

		moon_dude = sem.get_moon_dude()
		self.title=Label(master,text=moon_dude)
		self.title.pack()
		# w.pack()
		# field=Entry(master)
		# field.pack()
		master.mainloop()
