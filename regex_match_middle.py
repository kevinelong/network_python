import re

descriptions = [
    "GigabitEthernet0/0/3.60 CUR:,ATT:IZEP556112 ATI,H,ETH:200MB,MPLS,ATT",
    "GigabitEthernet0/0/3.60 CUR:,ATT:IZEP556112 ATI,H,ZZZ:200gib ,MPLS,ATT",
    "GigabitEthernet0/0/3.60 CUR:,ATT:IZEP556112 ATI,H,ETH: 200mb,MPLS,ATT",
]

#p = re.compile(r'.*,\s*(\d)[mbMBgbGBiI]*\s*,.*')
p = re.compile(r',.*:[\s]*(\d*)[mbMBgbGBiI]*\s*,')
for d in descriptions:
    m = p.search(d)
    if m:
        print(m.groups())

text = "GigabitEthernet0/0/3.60 CUR:,ATT:IZEP556112 ATI,H,ETH:200MB,MPLS,ATT"
