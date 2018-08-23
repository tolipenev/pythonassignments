# Classes and Objects NetDevice Class
# A program that lets users add attributes to a device, save it and view all of them later
# Anatoli Penev
# 11.02.2018


class NetDevice:
    def __init__(self, name=None, mac_address=None, ip_address=None, mask=None, gateway=None):
        self.__name = name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__mask = mask
        self.__gateway = gateway

    def set_name(self, name):
        self.__name = name
        # This method assigns a value to the __name field.

    def set_mac_address(self, mac_address):
        self.__mac_address = mac_address
        # This method assigns a value to the __ mac_address field.

    def set_ip_address(self, ip_address):
        self.__ip_address = ip_address
        # This method assigns a value to the __ ip_address field.

    def set_mask(self, mask):
        self.__mask = mask
        # This method assigns a value to the __ mask field

    def set_gateWay(self, gateway):
        self.__gateway = gateway
        # This method assigns a value to the __ gateWay field

    def get_name(self):
        return self.__name
        # This method returns the value of the name field.

    def get_mac_address(self):
        return self.__mac_address
        # This method returns the value of the mac_address field.

    def get_ip_address(self):
        return self.__ip_address
        # This method returns the value of the ip_address field.

    def get_mask(self):
        return self.__mask
        # This method returns the value of the mask field.

    def get_gateWay(self):
        return self.__gateway
        # This method returns the value of the gateWay field.

    def tostring(self):
        return self.__name + " " + self.__mac_address + " " + self.__ip_address + " " + self.__mask + " " + self.__gateway


class Computer(NetDevice):
    def __init__(self, os=None, cpu=None, ram=None, name=None, mac_address=None, ip_address=None, mask=None, gateway=None):
        NetDevice.__init__(self, name, mac_address, ip_address, mask, gateway)
        self.__cpu = cpu
        self.__os = os
        self.__ram = ram
        
    def get_os(self):
        return self.__os
    
    def get_cpu(self):
        return self.__cpu
    
    def get_ram(self):
        return self.__ram
    
    def set_os(self, os):
        self.__os = os
            
    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_ram(self, ram):
        self.__ram = ram

    def tostring(self):
        return self.get_cpu() + " " + self.get_os() + " " + self.get_ram()+ " " + self.get_name() + " " + self.get_mac_address() + " " + self.get_ip_address() + " " + self.get_mask() + " " + self.get_gateWay()


def main():
    devices = load_from_file()

    while True:
        user_choice = input("Press 1 to add device or other number to exit: ")
        if not check(user_choice):
            continue
        if user_choice == "1":
            entry = user_entry()
            devices[entry.get_name()] = entry
        else:
            for key, device in devices.items():
                print("Device: ",device.get_cpu(), device.get_os(), device.get_ram(), device.get_name(), device.get_mac_address(), device.get_ip_address(), device.get_mask(),
                      device.get_gateWay())
            print("Exiting program")
            save_to_file(devices)
            exit()


def save_to_file(devices):
    f = open("computers.txt", "w+")
    for key, item in devices.items():
        f.write(item.tostring())
        print("Saved to file")


def load_from_file():
    import os.path
    dic = {}
    if os.path.isfile("computers.txt"):
        f = open('computers.txt', "r")
        lines = f.readlines()
        for line in lines:
            sp = line.split(" ")
            dic[sp[0]] = Computer(sp[0], sp[1], sp[2], sp[3], sp[4], sp[5], sp[6], sp[7])
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
    os = input("Please enter OS: ")
    cpu = input("Please enter CPU type: ")
    ram = input("Please enter ram size: ")
    name = input("Please enter name: ")
    mac_address = input("Please enter mac address: ")
    ip_address = input("Please enter ip address: ")
    mask = input("Please enter mask: ")
    gateway = input("Please enter gateway: ")
    return Computer(os, cpu, ram, name, mac_address, ip_address, mask, gateway)


main()