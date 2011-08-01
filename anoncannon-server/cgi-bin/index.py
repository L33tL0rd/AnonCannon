#!/usr/bin/python
#Just a buggy Web-Info-Panel
def read_from_file(file):
  fd=open(file)
  value=fd.read()
  fd.close()
  return value
print("Content-Type: text/html")
print 
print("<html><body><h1>AnonCannon InfoPanel!</h1><hr>")
active_user = 0
for i in range(1,5):
  active_user += int(read_from_file("tmp/group" + str(i)))
print("Current Active users:" + str(active_user) )
print("<br>")
