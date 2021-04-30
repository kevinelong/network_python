import creds
from policymaps import T1, LBW, MBW, HBW, LAN
from ciscoconfparse import CiscoConfParse
from time import sleep
import netmiko
import io
from os import getlogin
from multiprocessing.pool import Pool


def safe_commands(connection: object, commands: list) -> str:
    try:
        result = connection.send_command(commands)
#        print('result: ', result)
    except OSError:
        return 'OS Error'
    else:
        return result

def getconfig(packed):
    routerip = packed
    try:
        connection = netmiko.ConnectHandler(**creds.ESL_WAN, ip=routerip)
        assert isinstance(connection, netmiko.cisco.CiscoIosSSH)
    except netmiko.NetMikoAuthenticationException:
        return routerip, 'ERR:ConnectionFailure'
    except netmiko.NetMikoTimeoutException:
        return routerip, 'ERR:ConnectionFailure'
    else:
        print('Connected to', routerip)
        print('Gathering configuration ...')
        deviceconfig = safe_commands(connection, 'sh run')
        sleep(5)
        connection.disconnect()
        return [deviceconfig, routerip]


def validateconfigWAN(devconfig):
    parse = CiscoConfParse(io.StringIO(devconfig), syntax='ios')
    intf_hostname = parse.re_match_iter_typed(r'^hostname\s+(\S+)', default='')
    devpolicy = ''
    csize = '0'
    interface = ''
    output = ''
    hasShaper = False
    flag = False
    policy = ''
    cspeed = '0'
    returnpolicy = []
    returncspeed = []
    returninterface = []
    returnhasShaper = []
    returnflag = []


    for intf_obj in parse.find_objects('^interface'):
        intf_name = intf_obj.re_match_typed('^interface\s+(\S.+?)$')

        # Search children of all interfaces for a regex match and return
        # the value matched in regex match group 1.  If there is no match,
        # return a default value: ''

        intf_desc = intf_obj.re_match_iter_typed(r"( description (?P<description>.*))\n", result_type=str, group=2, default='')
        intf_policy = intf_obj.re_match_iter_typed(r'service-policy\soutput\s(\w+\-\w+\-\w+\-\w+)\s', result_type=str, group=1, default='')
        if intf_policy:
            output = output + "{0}\t{2}\t{1}".format(intf_name, intf_policy, intf_desc)
            interface = intf_name
            devpolicy = intf_policy
            desc = intf_desc.split(',')

            try:
                desc = desc[3]
            except:
                policy = 'Not a valid speed in circuit description'
                cspeed = 0
                result = 'Invalid Circuit Description'
                writefile = intf_hostname + '\t' + output + '\t' + result
                with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                    f.write(writefile)
                    f.write('\n')
                flag = True
                return [policy, cspeed, interface, hasShaper, flag, intf_hostname]

            desc = desc.split(':')

            try:
                csize = desc[1].strip('mbMBgG')
            except:
                policy = 'Not a valid speed in circuit description'
                cspeed = 0
                result = 'Invalid Circuit Description'
                writefile = intf_hostname + '\t' + output + '\t' + result
                with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                    f.write(writefile)
                    f.write('\n')
                flag = True
                return [policy, cspeed, interface, hasShaper, flag, intf_hostname]

            cspeed = float(csize)
            if cspeed == 1.5:
                policy = "QOS-WAN-T1-EGRESS"
            elif cspeed > 1.5 and cspeed <= 30:
                policy = "QOS-WAN-LBW-EGRESS"
            elif cspeed > 30 and cspeed <= 155:
                policy = "QOS-WAN-MBW-EGRESS"
            elif cspeed > 155:
                policy = "QOS-WAN-HBW-EGRESS"
            else:
                policy = "Not a valid speed in circuit description"

            for intf_obj in parse.find_objects(r'^\s*policy-map\s(\w+\-\w+\-\w+\-\w+)M'):
                intf_policy = intf_obj.re_match_typed(r'^\s*policy-map\s(\w+\-\w+\-\w+\-\w+)')
                if intf_policy == devpolicy:
                    hasShaper = True
                    childlist = parse.find_all_children(intf_obj.text)
                    x = 0
                    while x < len(childlist):
                        if 'service-policy' in childlist[x]:
                            devpolicy = childlist[x]
                            devpolicy = devpolicy.strip('service-policy ')
                            devpolicy = devpolicy.strip('\n')
                        x += 1

            if policy == devpolicy:
                result = 'Correct Policy'
            else:
                result = 'Incorrect Policy'

            writefile = intf_hostname + '\t' + output + '\t' + result
            with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                f.write(writefile)
                f.write('\n')
            output = ''
            returnpolicy.append(policy)
            returncspeed.append(cspeed)
            returninterface.append(interface)
            returnhasShaper.append(hasShaper)
            returnflag.append(flag)
            devpolicy = ''
            csize = '0'
            interface = ''
            output = ''
            hasShaper = False
            flag = False
            policy = ''
            cspeed = '0'

    return [returnpolicy, returncspeed, returninterface, returnhasShaper, returnflag, intf_hostname]

def QOSpushPMAP(list, routerip):
    i = 0
    length = len(list[2])
    update = True

    try:
        connection = netmiko.ConnectHandler(**creds.ESL_WAN, ip=routerip)
        assert isinstance(connection, netmiko.cisco.CiscoIosSSH)
    except netmiko.NetMikoAuthenticationException:
        return routerip, 'ERR:ConnectionFailure'
    except netmiko.NetMikoTimeoutException:
        return routerip, 'ERR:ConnectionFailure'
    else:
        while i < length:

            policy = list[0][i]
            cspeed = float(list[1][i])
            interface = 'interface ' + str(list[2][i])
            hasShaper = list[3][i]
            flag = list[4][i]
            hostname = list[5]

            if flag is True:
                writefile = hostname + '\t' + 'Could not update, check main log'
                with open('C:\\scripts_logs\\QoS2\\WANQoS\\' + username + '.log', 'a') as f:
                    f.write(writefile)
                    f.write('\n')
                connection.disconnect()
                return


            if cspeed % 1 == 0:
                cspeed = int(cspeed)
            cspeed = str(cspeed)

            RemoveQoS(policy, interface, hasShaper, cspeed, routerip)

            if policy == "QOS-WAN-T1-EGRESS":
                connection.send_config_set(T1)
                addconfig = [interface,
                            "service-policy output QOS-WAN-T1-EGRESS",
                ]
                connection.send_config_set(addconfig)
                print(hostname + ' Updated')
                update = True
            elif policy == "QOS-WAN-LBW-EGRESS":
                connection.send_config_set(LBW)
                if "Multilink" in interface:
                    addconfig = [interface,
                                 "service-policy output QOS-WAN-LBW-EGRESS",
                                 ]
                    connection.send_config_set(addconfig)
                    print(hostname + ' Updated')
                    update = True
                else:
                    addconfig = ["policy-map QOS-PARENT-SHAPER-" + cspeed + "M",
                            "class class-default",
                            "shape average " + cspeed + "000000",
                            "service-policy QOS-WAN-LBW-EGRESS",
                            interface,
                            "service-policy output QOS-PARENT-SHAPER-" + cspeed + "M",
                    ]
                    connection.send_config_set(addconfig)
                    print(hostname + ' Updated')
                    update = True
            elif policy == "QOS-WAN-MBW-EGRESS":
                connection.send_config_set(MBW)
                addconfig = ["policy-map QOS-PARENT-SHAPER-" + cspeed + "M",
                            "class class-default",
                            "shape average " + cspeed + "000000",
                            "service-policy QOS-WAN-MBW-EGRESS",
                            interface,
                            "service-policy output QOS-PARENT-SHAPER-" + cspeed + "M",
                            ]
                connection.send_config_set(addconfig)
                print(hostname + ' Updated')
                update = True
            elif policy == "QOS-WAN-HBW-EGRESS":
                connection.send_config_set(HBW)
                addconfig = ["policy-map QOS-PARENT-SHAPER-" + cspeed + "M",
                            "class class-default",
                            "shape average " + cspeed + "000000",
                            "service-policy QOS-WAN-HBW-EGRESS",
                            interface,
                            "service-policy output QOS-PARENT-SHAPER-" + cspeed + "M",
                ]
                connection.send_config_set(addconfig)
                print(hostname + ' Updated')
                update = True
            else:
                print("Invalid Policy")
                update = False

            if update is True:
                writefile = hostname + '\t' + 'Updated'
                with open('C:\\scripts_logs\\QoS2\\WANQoS\\' + username + '.log', 'a') as f:
                    f.write(writefile)
                    f.write('\n')
            else:
                writefile = hostname + '\t' + 'Invalid Policy'
                with open('C:\\scripts_logs\\QoS2\\WANQoS\\' + username + '.log', 'a') as f:
                    f.write(writefile)
                    f.write('\n')
            i += 1
        connection.disconnect()

def RemoveQoS(policy, interface, hasShaper, cspeed, routerip):

    try:
        connection = netmiko.ConnectHandler(**creds.ESL_WAN, ip=routerip)
        assert isinstance(connection, netmiko.cisco.CiscoIosSSH)
    except netmiko.NetMikoAuthenticationException:
        return routerip, 'ERR:ConnectionFailure'
    except netmiko.NetMikoTimeoutException:
        return routerip, 'ERR:ConnectionFailure'
    else:
        if hasShaper is True:
            addconfig = [interface,
                         'no service-policy output QOS-PARENT-SHAPER-' + cspeed + 'M',
                         'no policy-map QOS-PARENT-SHAPER-' + cspeed + 'M',
                         'no policy-map ' + policy,
                         ]
            connection.send_config_set(addconfig)
        else:
            addconfig = [interface,
                         'no service-policy output ' + policy,
                         'no policy-map ' + policy,
                         ]
            connection.send_config_set(addconfig)

    connection.disconnect()

def WANPMAPcounters(list, routerip):
    i = 0
    length = len(list[2])
    hostname = list[5]
    print('Gathering policy-map information for', routerip)

    try:
        connection = netmiko.ConnectHandler(**creds.ESL_WAN, ip=routerip)
        assert isinstance(connection, netmiko.cisco.CiscoIosSSH)
    except netmiko.NetMikoAuthenticationException:
        return routerip, 'ERR:ConnectionFailure'
    except netmiko.NetMikoTimeoutException:
        return routerip, 'ERR:ConnectionFailure'
    else:
        while i < length:
            interface = 'interface ' + str(list[2][i])
            pmapoutput = safe_commands(connection, 'sh policy-map ' + interface + ' | i Class-map|packets')

            writefile = hostname + '\n' + pmapoutput
            with open('C:\\scripts_logs\\QoS2\\PMAPcounters\\' + username + '.log', 'a') as f:
                f.write(writefile)
                f.write('\n')
            i += 1
    connection.disconnect()



def validateconfigLAN(devconfig):
    parse = CiscoConfParse(io.StringIO(devconfig), syntax='ios')
    intf_hostname = parse.re_match_iter_typed(r'^hostname\s+(\S+)', default='')
    interfaces = []


    for intf_obj in parse.find_objects('^interface'):
        intf_name = intf_obj.re_match_typed('^interface\s+(\S.+?)$')

        # Search children of all interfaces for a regex match and return
        # the value matched in regex match group 1.  If there is no match,
        # return a default value: ''

        intf_policy = intf_obj.re_match_iter_typed(r'service-policy\sinput\s(\w+\-\w+\-\w+)\s', result_type=str,
                                                   group=1, default='')
        if intf_policy:
            interfaces.append(intf_name)
            writefile = intf_hostname + '\t' + intf_name + '\t' + intf_policy
            with open('C:\\scripts_logs\\QoS2\\LAN\\' + username + '.log', 'a') as f:
                f.write(writefile)
                f.write('\n')

    return [intf_hostname, interfaces]


def QOSpushPMAPLAN(list, routerip):
    print(list[0])
    i = 0
    length = len(list[1])

    try:
        connection = netmiko.ConnectHandler(**creds.ESL_WAN, ip=routerip)
        assert isinstance(connection, netmiko.cisco.CiscoIosSSH)
    except netmiko.NetMikoAuthenticationException:
        return routerip, 'ERR:ConnectionFailure'
    except netmiko.NetMikoTimeoutException:
        return routerip, 'ERR:ConnectionFailure'
    else:
        while i < length:
            addconfig = [list[1][i],
                         'no service-policy input QOS-LAN-INGRESS']
            connection.send_config_set(addconfig)
            i += 1

        connection.send_command('no policy-map QOS-LAN-INGRESS')
        connection.send_config_set(LAN)

        i = 0

        while i < length:
            addconfig = [list[1][i],
                         'service-policy input QOS-LAN-INGRESS']
            connection.send_config_set(addconfig)
            i += 1

"""
Interact with the user to select (one or more tasks). Display results (also progress?).
Apply a Task to a list of device IPs and log the result-details for each device the task is run on.

NOUNS (people places things) - Classes/Modules
VERBS (Action Words) - Functions/Methods on the classes
ADJECTIVES (Describe) - Attributes/Properties

"""
if __name__ == '__main__':
    username = getlogin()
    select = input('''
    What would you like to accomplish?:
    1: Verify WAN QoS Interfaces/Policy
    2: Update WAN QoS Service Policy
    3: Verify LAN QoS Interfaces/Policy
    4: Update LAN QoS Service Policy
    5: Get WAN PMAP counters
    ''')
    if int(select) == 1:
        filepath = input('Enter file path of device IPs\n')
        with open(filepath, 'r') as f:
            routers = []
            input_file = f.read()
        input_file = input_file.split("\n")
        routers = [i for i in input_file if i != ''] #remove blank lines
        list_of_routers = [(target) for target in routers]
#        username = getlogin()
        with Pool(20) as p:
#            if False:
#                assert isinstance(p, Pool)
            for idx, res in enumerate(p.imap_unordered(getconfig, list_of_routers)):
                if 'ERR:ConnectionFailure' not in res[0]:
                    validateconfigWAN(res[0])
                else:
                    with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                        f.write(str(res[0]))
                        f.write('\n')
    elif int(select) == 2:
        filepath = input('Enter file path of device IPs\n')
        with open(filepath, 'r') as f:
            routers = []
            input_file = f.read()
        input_file = input_file.split("\n")
        routers = [i for i in input_file if i != '']
        list_of_routers = [(target) for target in routers]
#        username = getlogin()
        with Pool(10) as p:
#            if False:
#                assert isinstance(p, Pool)
            for idx, res in enumerate(p.imap_unordered(getconfig, list_of_routers)):
                if 'ERR:ConnectionFailure' not in res[0]:
                    list = validateconfigWAN(res[0])
                    QOSpushPMAP(list, res[1])
                else:
                    with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                        f.write(str(res[0]))
                        f.write('\n')
    elif int(select) == 3:
        filepath = input('Enter file path of device IPs\n')
        with open(filepath, 'r') as f:
            routers = []
            input_file = f.read()
        input_file = input_file.split("\n")
        routers = [i for i in input_file if i != '']
        list_of_routers = [(target) for target in routers]
        with Pool(10) as p:
#            if False:
#                assert isinstance(p, Pool)
            for idx, res in enumerate(p.imap_unordered(getconfig, list_of_routers)):
                if 'ERR:ConnectionFailure' not in res[0]:
                    validateconfigLAN(res[0])
                else:
                    with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                        f.write(str(res[0]))
                        f.write('\n')
    elif int(select) == 4:
        filepath = input('Enter file path of device IPs\n')
        with open(filepath, 'r') as f:
            routers = []
            input_file = f.read()
        input_file = input_file.split("\n")
        routers = [i for i in input_file if i != '']
        list_of_routers = [(target) for target in routers]
#        username = getlogin()
        with Pool(10) as p:
#            if False:
#                assert isinstance(p, Pool)
            for idx, res in enumerate(p.imap_unordered(getconfig, list_of_routers)):
                if 'ERR:ConnectionFailure' not in res[0]:
                    list = validateconfigLAN(res[0])
                    QOSpushPMAPLAN(list, res[1])
                else:
                    with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                        f.write(str(res[0]))
                        f.write('\n')
    elif int(select) == 5:
        filepath = input('Enter file path of device IPs\n')
        with open(filepath, 'r') as f:
            routers = []
            input_file = f.read()
        input_file = input_file.split("\n")
        routers = [i for i in input_file if i != '']
        list_of_routers = [(target) for target in routers]
#        username = getlogin()
        with Pool(10) as p:
            #            if False:
            #                assert isinstance(p, Pool)
            for idx, res in enumerate(p.imap_unordered(getconfig, list_of_routers)):
                if 'ERR:ConnectionFailure' not in res[0]:
                    list = validateconfigWAN(res[0])
                    WANPMAPcounters(list, res[1])
                else:
                    with open('C:\\scripts_logs\\QoS2\\' + username + '.log', 'a') as f:
                        f.write(str(res[0]))
                        f.write('\n')
    else:
        print('Invalid Selection')