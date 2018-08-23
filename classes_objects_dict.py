# Classes and Objects NetDevice Class
# A program that lets users add attributes to a device, save it and view all of them later
# Anatoli Penev
# 11.02.2018


class NetDevice:
    def __init__(self, name=None, macAddress=None, ipAddress=None, mask=None, gateWay=None):
        self.__name = name
        self.__macAddress = macAddress
        self.__ipAddress = ipAddress
        self.__mask = mask
        self.__gateway = gateWay

    def set_name(self, name):
        self.__name = name
        #This method assigns a value to the __name field.
    def set_macAddress(self, macAddress):
        self.__macAddress = macAddress
        #This method assigns a value to the __ macAddress field.
    def set_ipAddress(self, ipAddress):
        self.__ipAddress = ipAddress
        #This method assigns a value to the __ ipAddress field.
    def set_mask(self, mask):
        self.__mask = mask
        #This method assigns a value to the __ mask field
    def set_gateWay(self, gateway):
        self.__gateway = gateway
        #This method assigns a value to the __ gateWay field
    def get_name(self):
        return self.__name
        #This method returns the value of the name field.
    def get_macAddress(self):
        return self.__macAddress
        #This method returns the value of the macAddress field.
    def get_ipAddress(self):
        return self.__ipAddress
        #This method returns the value of the ipAddress field.
    def get_mask(self):
        return self.__mask
        #This method returns the value of the mask field.
    def get_gateWay(self):
        return self.__gateway
        #This method returns the value of the gateWay field.
    def tostring(self):
        return self.__name + " " + self.__macAddress + " " + self.__ipAddress + " " + self.__mask + " " + self.__gateway


def main(): 
    devices =load_from_file()

    while True:
        userchoice = input("Press 1 to add device or other number to exit: ")
        if not check(userchoice):
            continue   
        if userchoice == "1":
            entry=user_entry()
            devices[entry.get_name()]=entry
        else:
            for key, device in devices.items():
                print("Device: ", device.get_name(), device.get_macAddress(), device.get_ipAddress(), device.get_mask(), device.get_gateWay())
            print("Exiting program")
            save_to_file(devices)
            exit()


def save_to_file(devices):  
    f = open("netdevices.txt", "w+")
    for key, item in devices.items():
        f.write(item.tostring())
        print("Saved to file")


def load_from_file():
    import os.path
    dic = {}
    if os.path.isfile("computer.txt"):
        f= open('netdevices.txt')
        lines = f.readlines()
        for line in lines:
            sp=line.split(" ")
            dic[sp[0]]=NetDevice(sp[0],sp[1],sp[2],sp[3],sp[4])
    return dic


def check(s):
    import re
    try:
        if not re.match("^[0-9_-]*$", s):
            raise TypeError
        return True
    except TypeError:
        print("Only digits are accepted!")
        return False

def user_entry():
    name = input("Please enter name: ") 
    mac_address = input("Please enter mac address: ") 
    ip_address = input("Please enter ip address: ")
    mask = input("Please enter mask: ") 
    gateway = input("Please enter gateway: ") 
    return NetDevice(name, mac_address, ip_address, mask, gateway)


main()