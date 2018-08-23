# The Contact class holds contact information.

class NetDevice:
    # The __init__ method initializes the attributes.
    def __init__(self, name, macAddress, ipAddress):
        self.__name = name
        self.__macAddress = macAddress
        self.__ipAddress = ipAddress

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_macAddress method sets the macAddress attribute.
    def set_macAddress(self, macAddress):
        self.__macAddress = macAddress

    # The set_ipAddress method sets the ipAddress attribute.
    def set_ipAddress(self, ipAddress):
        self.__ipAddress = ipAddress

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_macAddress method returns the macAddress attribute.
    def get_macAddress(self):
        return self.__macAddress

    # The get_ipAddress method returns the ipAddress attribute.
    def get_ipAddress(self):
        return self.__ipAddress

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nmacAddress: " + self.__macAddress + \
               "\nipAddress: " + self.__ipAddress
    
