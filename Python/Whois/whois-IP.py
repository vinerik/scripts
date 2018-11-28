#!/usr/bin/python

from netaddr import *
import whois
import ipcalc
import time

vStartIP = IPAddress('5.0.0.0')
vNew_IP = IPAddress('5.0.0.0')
vStart_Network('5.0.0.0/8')

w = whois.whois(str(vStartIP))
print w
vNet_Start = IPNetwork('1.0.0.0/1')
vCurrent_Net = ipcalc.Network(w.route)
print w.route,w.origin,w.country_RIPE,w.organization,w.address1,w.descr,w.netname

for i in range(16777216):
#for i in range(16):
	#vCurrent_Net = ipcalc.Network(w.route)
	if vCurrent_Net.has_key(str(vNew_IP)):	
		#print "I = " + str(i)
		print "vNew_IP : " + str(vNew_IP)
		#vNew_IP = IPNetwork(str(vStartIP)/8)[+i]
		vNew_IP = IPNetwork(str(vNew_IP)+"/8")[+i]
		print "IP" + str(vNew_IP) + "Subnet: " + w.route + "Usable IP: " + (str(vCurrent_Net.size()))
  		#i = (vCurrent_Net.size())
	else:
		print "vNew_IP : " + str(vNew_IP)
		vCurrent_Net = ipcalc.Network(str(vNew_IP)+"/8")
		IPNetwork(str(vNew_IP)+"/8")[+i]
		w = whois.whois(str(vNew_IP))	
		print w.route,w.origin,w.country_RIPE,w.organization,w.address1,w.descr,w.netname
		vNew_IP = w.route
		time.sleep(5)
