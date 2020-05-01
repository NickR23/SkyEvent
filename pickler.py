import pickle

def save( obj, name ):
  with open('obj/' + name + '.pkl', 'wb') as f:
    pickle.dump( obj, f, pickle.HIGHEST_PROTOCOL)

def load( name ):
  with open('obj/' + name + '.pkl', 'rb') as f:
    return pickle.load(f)


#maps to name and number of args expected in list
dict = {
  '-u':['utc', 2 ],
  '-la':['lat', 1], #Signifies lat lon input next
  '-lo':['lon', 1], #longitude
  '-n':['ns', 1 ], #Direction of lat
  '-e':['ew', 1], #Direction of lon
  '-c':['coords', 1], #On/Off ecliptic and equator
  '-m':['moonp', 1], #On/Off moon and planets
  '-dc':['deep', 1], #On/Off deep sky objects followed by magnitude value
  '-dv':['deepm', 1],
  '-o':['consto', 1], #On/Off constellation outlines
  '-cn':['constn', 1], #OnOff constellation names
  '-ca':['consta', 1], #On/Off align names with horizon
  '-cs':['consts', 1], #On/Off abbreviate constellation names
  '-cb':['constb', 1],#On/Off show constellation bounds
  '-sm':['limag', 1], #Lower bound for mag of stars displayed
  '-sn':['starn', 1],#On/Off star names
  '-snm':['starnm', 1],#Lower bound for mag of named stars
  '-sb':['starb', 1],#On/Off for Bayer codes 
  '-sbm':['starbm', 1], #Lower bound for mag of Bayer labeled stars
  '-i':['flip', 1], #Invert South and North
  '-is':['imgsize', 1], #Set size of output image
  '-f':['fontscale', 1],#Set font size
  '-co':['scheme', 1],#Set scheme (colour, bw, wb, red)
  }
save( dict, 'flags' )

