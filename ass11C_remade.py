import pickle
import computer
import os
import json
import netdevice

LOOK_UP     = 1
ADD         = 2
CHANGE      = 3
DELETE      = 4
LIST_ALL    = 5
QUIT        = 6

device_file = 'networkdevice.json'

def main():

    devices = load_netDevices()
    choice = 0
    while choice != QUIT:
    
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(devices)
        elif choice == ADD:
            devices = add(devices)
        elif choice == CHANGE:
            devices = change(devices)
        elif choice == DELETE:
            devices = delete(devices)
        elif choice == LIST_ALL:
            devices = list_all(devices)
    save_netDevices(devices)
    os.system('cls')

def list_all(netDevice_dct):
    for name in netDevice_dct:
        print_computer_object(netDevice_dct,name)

    
def load_netDevices():
    try:
        input_file = open('computer.json','w')
           # json.dump(input_file,outfile)
        open(device_file,'rb')
        netDevice_dct = pickle.load(input_file)
        input_file.close()        
    except IOError:
        netDevice_dct = {}
        print('Making myself cry in the corner')
    return netDevice_dct
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a netDevice')
    print('2. Add a new netDevice')
    print('3. Change an existing netDevice')
    print('4. Delete a netDevice')
    print('5. List all of the devices')
    print('6. Quit')
    print()

    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice'))
    return choice

########add get_ip and other shit here
def print_computer_object(netDevice_dct, name):
    print("Name: ", netDevice_dct[name].get_name())
    print("MAC: ", netDevice_dct[name].get_mac())
    print("Ram size: ", netDevice_dct[name].get_ram())
    print("IP: ", netDevice_dct[name].get_ipAddress())


def look_up(devices):
    name = input('Enter a name: ')
    print_computer_object(devices.get(name, 'That name is not found.'))
    

def add(devices):
    name = input('Name: ')
    macAddress = input('macAddress: ')
    ipAddress = input('ipAddress: ')
    cpu = input ('Enter cpu type and its speed: ')
    ram = input ('RAM size: ')
    os = input('Operating system: ')
    entry = computer.Computer(os,cpu,ram,name,macAddress,ipAddress)                        
    if name not in devices:
        devices[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')
    return devices

def change(devices):
    name = input('Enter a name: ')
    if name in devices:
        macAddress = input('Enter the new macAddress number: ')
        ipAddress = input('Enter the new ipAddress address: ')
        cpu = input ('Enter cpu type and its speed: ')
        ram = input ('RAM size: ')
        os = input('Operating system: ')
        entry = computer.Computer(os,cpu,ram,name,macAddress,ipAddress)
        devices[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')
    return devices

def delete(devices):
    name = input('Enter a name: ')
    if name in devices:
        del devices[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')
    return devices

def save_netDevices(devices):
    output_file = open(device_file, 'wb')

    pickle.dump(devices, output_file)

    output_file.close()
main()

