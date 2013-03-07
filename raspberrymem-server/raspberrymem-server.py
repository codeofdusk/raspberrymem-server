#import modules
from sys import argv
from sys import exit
import random
import socket
import pickle

#variable declarations
devices=[]

#function declarations
def find_device(id2find):
    for d2i in (devices):
        if (d2i.id == id2find ):
            return d2i
    #OK, we're here, so that means we didn't return from the for loop. Return 0 since no devices matched our search.
    return 0

#class declarations
class device(object):
    def __init__(self, id, reminders, notes, welfare_checking):
        #update devices list
        devices.append(self)
        #print information about this new device to stdout(will make more informative later if needed)
        print("new device registered with id",id," now the database contains ",len(devices)," devices.")

#do we have all required arguments?
if (len(argv) < 2 ):
    print("No port specified. Exiting")
    exit(1)
#OK, we have the port number, so let's set up our TCP socket
print("initializing socket...")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("binding...")
soc.bind((socket.gethostname(), int(argv[1])))
print("listening...")
soc.listen(5)
print("ready for incoming connections")
while (1) :
    con, addr = soc.accept()
    print("incoming connection from ",addr[0])
    #initial command ; what do we do?
    cmd=con.recv(3)
    if (cmd == b"reg" ):
        #create a new device
        #generate a very random ID
        multiplier=random.randint(10,1000)
        multiplier2=random.random()
        id=int(multiplier*multiplier2)
        #and finally, create an instance of the device class
        device = device(id,[],[],0)
        #now, print the id to the connection and close it
        idstr=str(id)
        con.send(bytes(idstr,"utf-8"))
        con.close()

