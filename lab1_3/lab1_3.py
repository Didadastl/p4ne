from pysnmp.hlapi import *

obj_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
obj_ver2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(), CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.209', '161')), ContextData(), ObjectType(obj_ver2))

for i in result:
    print(i)