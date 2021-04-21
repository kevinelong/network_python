from netmiko import ConnectHandler
import os
os.environ["NET_TEXTFSM"] = "d:/python37/lib/site-packages/ntc_templates/templates"
linux = {
    'device_type': 'linux',
    'host': '3.81.60.164',
    'username': 'kevin',
    'password': 'S!mpl312',
}
c = ConnectHandler(**linux)  # use of kwargs optional, could just use regular parameters
r = c.send_command("arp -a", use_textfsm=True)

print(r)
print(r[0]["ip_address"])

for item in r:
    print(item)
    print(item["ip_address"])

"""
EXPECTED OUTPUT:
[{'rev_dns': '_gateway', 'ip_address': '172.30.1.1', 'mac_address': '0e:18:8d:7f:b8:65', 'hw_type': 'ether', 'interface': 'eth0'}]
"""
# C:\Users\kevin\ntc-templates

# from netmiko import ConnectHandler
# import paramiko
# private_key_path = "~/.ssh/clvrclvr.pem"
# linux = {
#     'device_type': 'linux',
#     'host':   'clvrclvr.com',
#     'username': 'kevin',
#     'password': 'S!mpl312',
#     'pkey' : paramiko.RSAKey.from_private_key_file(private_key_path)
# }
# c = ConnectHandler(**linux) # use of kwargs optional, could just use regular parameters

# r = c.send_command("arp -a")
