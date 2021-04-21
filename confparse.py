from getpass import getpass
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

'''
Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration
into CiscoConfParse.
'''
password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)

show_run = net_connect.send_command("show run")
net_connect.disconnect()
cisco_cfg = CiscoConfParse(show_run.splitlines())

interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

print()
for i in interfaces:
    print("Interface: {}".format(i.text))
    ip_address = i.re_search_children(r"ip address")[0].text
    print("IP Address: {}".format(ip_address))
    print()
print()
