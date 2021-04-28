# pip install pyyaml

import yaml

data = """
-
  - HTML
  - LaTeX
  - SGML
  - VRML
  - XML
  - YAML
-
  - BSD
  - GNU Hurd
  - Linux
"""

raw = yaml.load(data)

print(raw)
# EXPECTED
# [['HTML', 'LaTeX', 'SGML', 'VRML', 'XML', 'YAML'], ['BSD', 'GNU Hurd', 'Linux']]


documents = """
name: The Set of Gauntlets 'Pauraegen'
description: >
 A set of handgear with sparks that crackle
 across its knuckleguards.
extra:
    this: thing
    that: other-thing
"""

raw = yaml.load(documents)

print(raw)
# EXPECTED
# {'name': "The Set of Gauntlets 'Pauraegen'", 'description': 'A set of handgear with sparks that crackle across its knuckleguards.\n', 'extra': {'this': 'thing', 'that': 'other-thing'}}

esphome_home_power_data = """
esphome:
  name: test
  platform: ESP32
  board: nodemcu-32s
wifi:
  ssid: "test"
  
  password: "test"
  
  manual_ip:
    static_ip: 192.168.1.251
    gateway: 192.168.1.1
    subnet: 255.255.255.0
    dns1: 192.168.1.1
  
# Enable logging
logger:
# Enable Home Assistant API
api:
  password: "test"
ota:
  password: "test"
spi:
  clk_pin: 18
  miso_pin: 19
  mosi_pin: 23
"""
raw = yaml.load(esphome_home_power_data)

print(raw)

import pprint

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(raw)
