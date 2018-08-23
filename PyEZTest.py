# Test program for the Device class by Per
from jnpr.junos import Device
# import base64 # to encrypt password
#import myPassword
#import base64

try:
    # Create device object
    mySRX_password = base64.b64decode(myPassword.getPassword())
    print('Testing if device can be created')
    myDev = Device(host='192.168.1.1', user='root', password=Toli90)
    print('Okay, device is created. Now testing reachable...')
    myDev.auto_probe = 3        # Test for 3 seconds if device is reachable
    print('Okay, device is reachable. Now trying to connect...')
    myDev.open()                # Connect to device
    print('Okay, connected. Sending cli command.')
    SRX_interface = myDev.cli("show interfaces terse", warning=False)  # Disable warnings
    print(SRX_interface)
    myDev.close()
except Exception as somethingWentWrong:
    print(somethingWentWrong)
