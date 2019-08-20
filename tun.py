from tuntap import TunTap


tun = TunTap(nic_type='Tun', nic_name='mytun')
tap = TunTap(nic_type='Tap', nic_name='mytap')
tap.config(ip="192.168.137.1",mask="255.255.255.240")
buf = tun.read(1500)
tun.write(buf)
