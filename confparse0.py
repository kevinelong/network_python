# http://www.pennington.net/py/ciscoconfparse/intro.html
# http://pennington.net/tutorial/ciscoconfparse/ccp_tutorial.html#slide1
# https://github.com/mpenning/ciscoconfparse
# pip install CiscoConfParse
from ciscoconfparse import CiscoConfParse

f = open("./cisco_config_examples/sample01.conf", "r")
cisco_cfg = CiscoConfParse(f.read().splitlines(keepends=False))

interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

print()
for i in interfaces:
    print("Interface: {}".format(i.text))
    ip_address = i.re_search_children(r"ip address")[0].text
    print("IP Address: {}".format(ip_address))
    print()
print()

print(cisco_cfg)
