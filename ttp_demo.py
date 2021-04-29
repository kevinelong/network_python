# DOCS: https://ttp.readthedocs.io/en/latest/index.html
from ttp import ttp

data_to_parse = """
interface Loopback0
 description Router-id-loopback
 ip address 192.168.0.113 255.255.255.255
!
interface Vlan778
 description CPE_Acces_Vlan
 ip address 2002::fd37/124
 ip vrf CPE1
!
"""

ttp_template1 = """ #SIMPLE
interface {{ interface }}
 ip address {{ ip }} {{ mask }}
 description {{ description }}
 ip vrf {{ vrf }}
"""
# create parser object and parse data using template:
parser = ttp(data=data_to_parse, template=ttp_template1)
parser.parse()

# SUPPORT BOTH IP4 and IP6 with masks delimited by / or space using regex
ttp_template2 = """
interface {{ interface }}
 ip address {{ ip }}{{separator | re("[ /]") }}{{ mask }}
 description {{ description }}
 ip vrf {{ vrf }}
"""

# create parser object and parse data using template:
parser = ttp(data=data_to_parse, template=ttp_template2)
parser.parse()

# print result in JSON format
for item in parser.result(format='json'):
    print(item)
# [
#     [
#         {
#             "description": "Router-id-loopback",
#             "interface": "Loopback0",
#             "ip": "192.168.0.113",
#             "mask": "24"
#         },
#         {
#             "description": "CPE_Acces_Vlan",
#             "interface": "Vlan778",
#             "ip": "2002::fd37",
#             "mask": "124",
#             "vrf": "CPE1"
#         }
#     ]
# ]

# or in csv format
csv_results = parser.result(format='csv')[0]
print(csv_results)
# description,interface,ip,mask,vrf
# Router-id-loopback,Loopback0,192.168.0.113,24,
# CPE_Acces_Vlan,Vlan778,2002::fd37,124,CPE1


# ---


ttp_template_location = """
snmp-server location {{host}},{{street | re("PHRASE")}},{{city | re("ORPHRASE")}},{{state | re("WORD")}},{{zip | _line_}}
 """
data = "snmp-server location LAS-ZZ-RT1-LASVEGAS-NV,6900 North Pecos Road,Las Vegas,NV,89086"
raw = ttp(data=data, template=ttp_template_location)
raw.parse()

output = raw.result(format='raw')
print(output)

###
ttp_template_boot_system = "boot system {{boot_IOS | _line_}}"

# 'show run | i boot system'

show_boot = """
boot system flash bootflash:asr1000rp1-adventerprisek9.03.16.10.S.155-3.S10-ext.bin
boot system bootflash:asr1000rp1-adventerprisek9.03.16.08.S.155-3.S8-ext.bin
"""

boot_raw = ttp(data=show_boot, template=ttp_template_boot_system)

boot_raw.parse()

output = boot_raw.result(format='raw')[0]

print(output)
