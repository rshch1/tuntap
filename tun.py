import os
from fcntl import ioctl
import struct
from pyroute2 import IPRoute

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_NO_PI = 0x1000

ftun = os.open("/dev/net/tun", os.O_RDWR)
ioctl(ftun, TUNSETIFF, struct.pack("16sH", b"tun0", IFF_TUN | IFF_NO_PI))


ip = IPRoute()
idx = ip.link_lookup(ifname='tun0')[0]
ip.addr('add', index=idx, address='192.168.137.1', prefixlen=28)
ip.link('set', index=idx, state='up')
while True:
    packet = list(os.read(ftun, 2048))
    packet[12:16], packet[16:20] = packet[16:20], packet[12:16]
    os.write(ftun, ''.join(packet))
ip.close()

