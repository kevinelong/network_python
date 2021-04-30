# https://scapy.readthedocs.io/en/latest/index.html
# pip install scapy

from scapy.all import *

packets = rdpcap('pcap_example.pcap')
print(len(packets))
for s in packets.sessions():
    print(s)

for packet in packets:
    print(packet.time, packet.name, packet.src, packet.dst, packet.layers(), packet[IP], packet.fields)

