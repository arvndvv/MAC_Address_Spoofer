# MAC-Address-Spoofer
>BETABRAIN is My CodeName
```
A tool to change MAC address of your machine,works for Linux Machines only.
Mainly Two options 
Run as Admin

sudo python3  main.py

- [x] give a custom valid MAC address by yourslef
or 
- [x] Generate random one

```
![MACSpoofer](macspoofer.png)

# Working
It executes the following commands
1. ifconfig. //to find the interface name
2. Ifconfig enp2s0 down. //Assume enp2s0 is our interface name, for this example( in program user can provide )
3. ifconfig enp2s0 hw ether 00:00:00:00:00:01.
4. ifconfig enp2s0 up.
