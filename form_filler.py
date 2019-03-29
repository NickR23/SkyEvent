from mechanize import Browser
import pickler

def string_or_bool( string, control):
  pos = ['true', 'True', 'y', 'yes']
  neg = ['false', 'False', 'n', 'no']
  if (control.type == 'checkbox'):
    result = ['on'] if string in pos else []
    return result
  if (control.type == 'text'):
    print(string)
    return str(string)
  if (string in pos) or (string in neg):
    return string in pos
  else:
    return string

def fill_form( br, argv ):
  #Remove first irrelevant arg
  argv.pop(0)
  argc = len( argv )

  #Load flag map
  flags = pickler.load( 'flags')

  #Selects the form we want
  br.form = list(br.forms())[0]
  
  for control in br.form.controls:
    print("name=%s, type=%s, value=%s" % (control.name, control.type, control.value))
    
#   Set dynimg so we just get an image instd of a map
  control = br.form.find_control("dynimg")
  control.items[0].selected=True
  is_text = False;
  control
  for index, arg in enumerate( argv ):
    if arg in flags:
      name = flags[ arg ][0]
      control = br.form.find_control( name )
    else:  
      control.value = string_or_bool([argv[index]], control)

  
  
#   Set color scheme
#   control = br.form.find_control("scheme")
#   control.value=["3"]
#   Disable star names
#   br.form.find_control("starn").items[0].selected=False
#   Disable boundaries
#   br.form.find_control("constb").items[0].selected=False
#   Disable names
#   br.form.find_control("constn").items[0].selected=False
#   Disable coords
#   br.form.find_control("coords").items[0].selected=False
#   
#   Set lat and lon values
#   lat = '0'
#   lon = '0'
#   if argc > 1:
#     lon = argv[1]
#   if argc > 2:
#     lat = argv[2]
#   control = br.form.find_control("lat")
#   control.value = lat
# 
#   control = br.form.find_control("lon")
#   control.value = lon
