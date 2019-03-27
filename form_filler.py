from mechanize import Browser
import pickler

def fill_form( br, argv ):
  #Remove first irrelevant arg
  argv.pop(0)
  argc = len( argv )

  #Load flag map
  flags = pickler.load( 'flags')

  #Selects the form we want
  br.form = list(br.forms())[0]
  
  #for control in br.form.controls:
    #print("name=%s, type=%s" % (control.name, control.type))
    
#   Set dynimg so we just get an image instd of a map
  control = br.form.find_control("dynimg")
  control.items[0].selected=True
  
  for index, arg in enumerate( argv ):
    if arg in flags:
      name = flags[ arg ]
      control = br.form.find_control( name )
    else:  
      control.value = [argv[index]]

  
  
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
