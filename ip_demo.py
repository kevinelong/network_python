import ipaddress

# https://docs.python.org/3/library/ipaddress.html


# Creating an object of IPv4Address class and
# initializing it with an IPv4 address.
ip = ipaddress.IPv4Address('112.79.234.30')
# ip2 = ipaddress.IPv6Address('112.79.234.30')

# Print total number of bits in the ip.
print("Total no of bits in the ip:", ip.max_prefixlen)

# Print True if the IP address is reserved for multicast use.
print("Is multicast:", ip.is_multicast)

# Print True if the IP address is allocated for private networks.
print("Is private:", ip.is_private)

# Print True if the IP address is global.
print("Is global:", ip.is_global)

# Print True if the IP address is unspecified.
print("Is unspecified:", ip.is_unspecified)

# Print True if the IP address is otherwise IETF reserved.
print("Is reversed:", ip.is_reserved)

# Print True if the IP address is a loopback address.
print("Is loopback:", ip.is_loopback)

# Print Ture if the IP address is Link-local
print("Is link-local:", ip.is_link_local)

# next ip address
ip1 = ip + 1
print("Next ip:", ip1)

# previous ip address
ip2 = ip - 1
print("Previous ip:", ip2)

# Print True if ip1 is greater than ip2
print("Is ip1 is greater than ip2:", ip1 > ip2)


###  NETWORK
print("---NETWORK---")

# Initializing an IPv4 Network.
network = ipaddress.IPv4Network("192.168.1.0/24")

# Print the network address of the network.
print("Network address of the network:", network.network_address)

# Print the broadcast address
print("Broadcast address:", network.broadcast_address)

# Print the network mask.
print("Network mask:", network.netmask)

# Print with_netmask.
print("with netmask:", network.with_netmask)

# Print with_hostmask.
print("with_hostmask:", network.with_hostmask)

# Print Length of network prefix in bits.
print("Length of network prefix in bits:", network.prefixlen)

# Print the number of hosts under the network.
print("Total number of hosts under the network:", network.num_addresses)

# Print if this network is under (or overlaps) 192.168.0.0/16
print("Overlaps 192.168.0.0/16:", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))

# Print the supernet of this network
print("Supernet:", network.supernet(prefixlen_diff=1))

# Print if the network is subnet of 192.168.0.0/16.
print("The network is subnet of 192.168.0.0/16:",
      network.subnet_of(ipaddress.IPv4Network("192.168.0.0/16")))

# Print if the network is supernet of 192.168.0.0/16.
print("The network is supernet of 192.168.0.0/16:",
      network.supernet_of(ipaddress.IPv4Network("192.168.0.0/16")))

# Compare the ip network with 192.168.0.0/16.
print("Compare the network with 192.168.0.0/16:",
      network.compare_networks(ipaddress.IPv4Network("192.168.0.0/16")))