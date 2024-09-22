#https://youtu.be/tW6rVHNHuJU?si=wblBQdEx-4gdey7z


#кол нуль/едениц
from ipaddress import *

net = ip_network('123.80.87.27/255.255.240.0',0)
address = f'{net.network_address:b}'
print(address.count('0'))

#кол комп

from ipaddress import *
net = ip_network('123.87.81.24/255.255.252.0',0)
num = net.num_addresses
print(num-2)

#номер компа
from ipaddress import *

ip = ip_address('123.87.81.24')
net = ip_network('123.87.81.24/255.255.240.0',0)
address = net.network_address
num = int(f'{ip:b}',2) - int(f'{address:b}',2)
print(num)


#второй слева байт
from ipaddress import *
for mask in range(32):
    net = ip_network(f'95.97.64.1/{mask}',0)
    address = ''.join(x for x in str(net.network_address))
    if address == '95.64.0.0':
        print(str(mask * '1' + ((32 - mask) * '0'))[8:])


import ipaddress as ipa
count = 0
net = ipa.ip_network('192.168.32.160/255.255.255.240', 0)
for ip in net:
    if format(ip, 'b').count('1') % 2 == 0:
        count += 1
print(count)




import ipaddress as ipa
net = ipa.ip_network('253.112.169.12/255.255.254.0', 0)
count = 0
for ip in net:
    if format(ip, 'b')[:16].count('1') <= format(ip, 'b')[16:].count('1'):
        count += 1
print(count)



from ipaddress import *


ip = ip_address('111.81.88.168')

for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if net[0] < ip < net[-1]:
        print(net, net.netmask)
#224



#11791
from ipaddress import *
from fnmatch import fnmatch

count = 0
ip = ip_address('246.51.128.202')
for mask in range(31):
    net = ip_network(f'{ip}/{mask}', 0)
    if fnmatch(f'{net.netmask}', '255.255.*.0'):
        if ip not in [net.network_address, net.broadcast_address]:
            if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
                print(net.netmask)




from ipaddress import *

for A in (128, 192, 224, 240, 248, 252, 254, 255):
    net = ip_network(f'238.51.1.202/255.255.{A}.0', 0)
    if ip_address('238.51.1.202') != net.network_address:
        if all(f'{ip:b}'[:16].count('1') >=  f'{ip:b}'[16:].count('1') for ip in net):
            print(A)
