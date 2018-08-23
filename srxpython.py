# Junos configuration script with Python and PyEZ
# Anatoli Penev
# 24.03.2018
# This program adds a static route configuration to a router.
# The configuration to be added is stored in a file named "srxpython.cfg"

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys  # To be able to exit with a system code in case of an error
hostIP = 'x.x.x.x'
configurationFile = "PATHTOFILE"
try:
    Device.auto_probe = 3
 # Instantiate a Device object
    dev = Device(host=hostIP,
                 user='',
                 password='',
                 gather_facts=False)

    print("Opening connection to " + hostIP)
    dev.open()
except Exception as somethingIsWrong:
    print("Something is wrong: ", somethingIsWrong)
    sys.exit(1)
 # Instantiate a Config(uration) object associated with the device
myConfig = Config(dev)
# Load and merge the configuration into the candidate configuration
try:
    myConfig.load(path=configurationFile,
                  format="text",
                  merge=True)  # be careful with: False
    print("Loading configuration to router done successfully")
    print(myConfig.diff())  # cli: show | compare
except Exception as loadFailed:
    print("Loading configuration failed: ", loadFailed)
sys.exit(1)
dev.close()
