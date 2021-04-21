from netmiko import ConnectHandler

linux = {
    'device_type': 'linux',
    'host': '54.224.250.13',
    'username': 'kevin',
    'password': 'S!mpl312',
}
c = ConnectHandler(**linux)  # use of kwargs optional, could just use regular parameters
r = c.send_command("arp -a", use_textfsm=True)
print(r)
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
