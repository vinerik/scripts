# Parse pcap data using thask and Python
content = !tshark -r network-troubleshooting.pcap -T fields -e data.data
#skip every other two
data = content[::2]
#
"".join([chr(int(c[2-:],16)) for c in data))

