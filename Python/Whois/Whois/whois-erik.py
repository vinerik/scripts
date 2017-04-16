#!/usr/bin/python

from netaddr import *
import whois
import ipcalc
import time


filename = "whois.log"
filehandle = open(filename, 'w')
vStartIP = IPAddress('5.0.0.0')
vNew_IP = IPAddress('5.0.0.0')

w = whois.whois(str(vStartIP))
vNet_Start = IPNetwork('1.0.0.0/1')
vCurrent_Net = ipcalc.Network(w.route)
filehandle.write( str(w.route) + "," + str(w.origin) + "," + str(w.country_RIPE)  + "," + str(w.organization) + "," + str(w.address) + "," + str(w.descr) + "," + str(w.netname) + "\n")
vNew_Subnet = w.route

for i in range(16777216):
	vCurrent_Net = ipcalc.Network(vNew_Subnet)
	if vCurrent_Net.has_key(str(vNew_IP)):	
		vNew_IP = IPNetwork(str(vNew_IP)+"/8")[+i]
	else:
		vCurrent_Net = ipcalc.Network(str(vNew_IP)+"/8")
		IPNetwork(str(vNew_IP)+"/8")[+i]
		w = whois.whois(str(vNew_IP))	
		if str(w.route) == "None":
			vNew_Subnet = str(vNew_IP)+"/24"
			filehandle.write( str(w.route) + "," + str(w.origin) + "," + str(w.country_RIPE)  + "," + str(w.organization) + "," + str(w.address) + "," + str(w.descr) + "," + str(w.netname) + "\n")
		else:
			vNew_Subnet = w.route
			filehandle.write( str(w.route) + "," + str(w.origin) + "," + str(w.country_RIPE)  + "," + str(w.organization) + "," + str(w.address) + "," + str(w.descr) + "," + str(w.netname) + "\n")
		time.sleep(3)
filehandle.close()
