# pip install textfsm
import textfsm

traceroute = '''
Type escape sequence to abort.
Tracing the route to 10.184.0.7
VRF info: (vrf in name/id, vrf out name/id)
  1 10.176.246.61 1 msec
    10.176.246.57 2 msec
    10.176.246.61 1 msec
  2 10.176.246.6 1 msec
    10.176.246.14 1 msec
    10.176.246.6 1 msec
  3 10.184.0.7 17 msec *  17 msec
'''

with open('traceroute.textfsm') as template:
    fsm = textfsm.TextFSM(template)  # use the file handle to create the fms object
    # result = fsm.ParseText(traceroute)  # use the fsm's ParseText method
    result = fsm.ParseTextToDicts(traceroute)  # use the fsm's ParseText method

print(fsm.header)
print(result)
print(len(result))
"""
EXPECTED OUTPUT
['ID', 'Hop']
[['1', '10.0.12.1'], ['2', '15.0.0.5'], ['3', '57.0.0.7'], ['4', '79.0.0.9']]
"""

# NET_TEXTFSM env variable to path to alternate to appdata for readability

"""
[{'address': '10.176.246.57',
  'details': '',
  'fqdn': '',
  'hop_num': '1',
  'rtt_response': ['89']},   
 {'address': '10.176.246.61',
  'details': '',
  'fqdn': '',
  'hop_num': '1',
  'rtt_response': ['3']},    
  'details': '',
  'fqdn': '',
  'hop_num': '1',
  'rtt_response': ['7']},
 {'address': '10.176.246.14',
  'details': '',
  'fqdn': '',
  'hop_num': '2',
  'rtt_response': ['1']},
 {'address': '10.176.246.6',
  'details': '',
  'fqdn': '',
  'rtt_response': ['1']},
 {'address': '10.176.246.14',
  'details': '',
  'fqdn': '',
  'hop_num': '2',
  'rtt_response': ['1']},
 {'address': '10.184.0.7',
  'details': '',
  'fqdn': '',
  'hop_num': '3',
  'rtt_response': ['17', '*', '17']}]
"""