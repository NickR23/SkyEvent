import pickle

def save( obj, name ):
  with open('obj/' + name + '.pkl', 'wb') as f:
    pickle.dump( obj, f, pickle.HIGHEST_PROTOCOL)

def load( name ):
  with open('obj/' + name + '.pkl', 'rb') as f:
    return pickle.load(f)



# dict = {
#   '-d':'date',
#   '-u':'utc',
#   '-j':'jd',
#   '-l':'lat lon', #Signifies lat lon input next
#   '-n':'ns', #Direction of lat
#   '-e':'ew', #Direction of lon
#   '-c':'coords', #On/Off ecliptic and equator
#   '-m':'moonp', #On/Off moon and planets
#   '-d':'deep', #On/Off deep sky objects followed by magnitude value
#   '-co':'conto', #On/Off constellation outlines
#   '-cn':'constn', #OnOff constellation names
#   '-ca':'consta', #On/Off align names with horizon
#   '-cs':'consts', #On/Off abbreviate constellation names
#   '-cb':'constb', #On/Off show constellation bounds
#   '-sm':'limag', #Lower bound for mag of stars displayed
#   '-sn':'starn', #On/Off star names
#   '-snm':'starnm', #Lower bound for mag of named stars
#   '-sb':'starb', #On/Off for Bayer codes 
#   '-sbm':'starbm', #Lower bound for mag of Bayer labeled stars
#   '-i':'flip', #Invert South and North
#   '-is':'imgsize', #Set size of output image
#   '-f':'fontscale', #Set font size
#   '-co':'scheme', #Set scheme (colour, bw, wb, red)
#   }
# save( dict, 'flags' )

