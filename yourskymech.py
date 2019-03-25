import mechanize as mech
br = mech.Browser()
res = br.open('http://www.fourmilab.ch/yoursky/')
#print(res.read())
#res = br.response()
for form in br.forms():
  print("Form name:", form.name)
  print(form)

