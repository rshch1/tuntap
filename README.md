# TUN device 

## General info
**Tun** is virtual network device interface. It acts just like a regular interface. Except we can hook to it and control it from userspace application.
**TUN** device is used to manipulate IP packets. 
This simple program up Tun device and assign 192.168.137.1 ip address to it. Network is 192.168.137.0/28.


## INSTALLATION and USAGE 

`pip install pyroute2`

Run program 
`sudo python tun_device.py`

Open another terminal  `ping 192.168.137.10`
