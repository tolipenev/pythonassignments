from netdevice import NetDevice

class Computer(NetDevice):
    def __init__(self,os,cpu,ramsize,name,macAddress,ipAddress):
        NetDevice.__init__(self,name,macAddress,ipAddress)
        self.__os = os
        self.__cpu = cpu
        self.__ramsize = ramsize
    def set_os(self,os):
        self.__os = operating_system
    def set_cpu(self,cpu):
        self.__cpu = cpu_typeNspeed
    def set_ramsize(self,ramsize):
        self.__ramsize = ram_size
    def get_os(self):
        return self.__os
    def get_cpu(self):
        return self.__cpu
    def get_ram(self):
        return self.__ramsize
    def __str__(self):
        return super().__str__()+ \
               "\n CPU: " + self.__cpu + \
               "\nOperating system: " + self.__os + \
               "\nRam size: " + self.__ramsize

