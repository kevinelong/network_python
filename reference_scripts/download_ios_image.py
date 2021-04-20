# Here is a
# more
# recent
# script
# for downloading an IOS image and ROMMON firmware if needed.This script uses two other includes that have the login credentials and one with dictionaries of the IOS and ROMMON versions, md5 hashes, files sizes.I also had to edit the txtfsm file for ‘show platform diag’ to include a firmware version (ROMMON version).The textfsm is below and the main script is after that.
#
# Value
# Filldown
# CHASSIS_TYPE(. *?)
#
# Value
# Required
# SLOT_NUMBER((?:.*)[A - Z]\d + (?:.*))
#
# Value
# MODULE_SKU(. +?)
#
# Value
# STATE(. +)
#
# Value
# RUNNING_STATE(. +)
#
# Value
# INTERNAL_STATE(. +)
#
# Value
# INTERNAL_OPERATIONAL_STATE(. +)
#
# Value
# INSERT_TIME(. *)
#
# Value
# UPTIME(. *)
#
# Value
# HARDWARE_SIGNAL(. *)
#
# Value
# PACKET_SIGNAL(. *)
#
# Value
# FIRMWARE_VERSION(. *)
#
#
#
# Start
#
# ^ Chassis
# type: ${CHASSIS_TYPE}(?:\s |$$)
#
# ^.*(?:Sub-slot | Slot):\s${SLOT_NUMBER}\, (?:\s${MODULE_SKU} | \s+$$)(?:\s + |$$)
#
# ^ \s + State\s *\:\s${STATE}
#
# ^.*Running
# state\s *\:\s${RUNNING_STATE}
#
# ^.*Internal
# state\s *\:\s${INTERNAL_STATE}
#
# ^.*Internal
# operational
# state\s *\:\s${INTERNAL_OPERATIONAL_STATE}
#
# ^.*Physical
# insert
# detect
# time\s *\:\s${INSERT_TIME}
#
# ^.*Software
# declared
# up
# time\s *\:\s${UPTIME}
#
# ^.*Hardware
# ready
# signal
# time\s *\:\s${HARDWARE_SIGNAL}
#
# ^.*Packet
# ready
# signal
# time\s *\:\s${PACKET_SIGNAL}
#
# ^.*Firmware
# version\s *\:\s${FIRMWARE_VERSION}
#
# # Capture time-stamp if vty line has command time-stamping turned on
#
# ^ Load\s +
# for \s+
#
# ^ Time\s + source\s + is
#
# ^ $$ -> Record

# Import modules

import logging

from ttp import ttp

from pprint import pprint

import netmiko

import creds

import textfsm

from os import getlogin

from multiprocessing.pool import ThreadPool

import re

from sys import argv

import time

import datetime

from keyboard import press

import wanos

import paramiko

ttp_template_boot_system = """

boot system {{boot_IOS | _line_}}

"""

# Define function to SSH to router using svc account and send 'copy scp to disk' command.

# Check version by router model type, check for any preexisting file in disk, and verify image after transfer

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

username = getlogin()

command_error = "******Commands failed******************"

connection_error = "******Connection failed******************"

timeout_error = '************Timeout Error**************'

authentication_error = '************Authentication Failure**************'

logname = f'C:\\SFTP_Root\\{username}.log'

logging.basicConfig(filename=logname,

                    filemode='a',

                    format='%(asctime)s %(levelname)s %(message)s',

                    datefmt='%H:%M:%S',

                    level=logging.ERROR)


def safe_commands(connection: object, commands: list) -> str:
    try:

        result = connection.send_command(commands)

    except OSError:

        with open(f'C:\\SFTP_Root\\{username}.log', 'a') as f:

            logging.error(command_error)

        print(f'\n\tERROR: {command_error}\n\n')

        return router

    else:

        return result


def sendCopy(packed):
    router, interface, source, auth_method = packed

    try:

        if auth_method == 'ESL_WAN1':

            connection = netmiko.ConnectHandler(**creds.ESL_WAN1, ip=router)

            assert isinstance(connection, netmiko.cisco.CiscoIosSSH)

        else:

            connection = netmiko.ConnectHandler(**creds.ESL_WAN, ip=router)

            assert isinstance(connection, netmiko.cisco.CiscoIosSSH)

    except netmiko.NetmikoAuthenticationException:

        return router, authentication_error

    except paramiko.ssh_exception.AuthenticationException:

        return router, authentication_error

    except netmiko.NetMikoTimeoutException:

        return router, timeout_error

    else:

        print('Connected to', router)

    show_ver = connection.send_command('show version', use_textfsm=True)
"""
[{'config_register': '0x2102',
  'hardware': ['ASR1004'],
  'hostname': 'LAS-ZZ-RT1-LASVEGAS-NV',
  'mac': [],
  'reload_reason': 'Reload Command',
  'rommon': 'IOS-XE',
  'running_image': 'asr1000rp1-adventerprisek9.03.16.08.S.155-3.S8-ext.bi',
  'serial': ['FOX1530GPRP'],
  'uptime': '2 weeks, 4 days, 18 hours, 22 minutes',
  'version': '15.5(3)S8'}]
"""
    # pprint(show_ver)

    host_name = show_ver[0]['hostname']

    print(f"Hostname: {host_name}")

    current_os_ver = ''

    new_rom_ver = ''

    client_commands = [f'ip http client source-interface {interface}', 'ip tcp path-mtu-discovery',
                       'ip tcp selective-ack', 'ip tcp window-size 65536', 'no file verify auto']

    no_client_commands = [f'no ip http client source-interface {interface}', 'no ip tcp path-mtu-discovery',
                          'no ip tcp selective-ack', 'no ip tcp window-size 65536']

    running_image = show_ver[0]['running_image']

    no_boot_out = ''

    for key in wanos.wanos:

        if key in running_image:
            filename = wanos.wanos.get(key)

            disk = wanos.wandisk.get(key)

            hash_value = wanos.md5_hash.get(key)

            ossize = wanos.wanossize.get(key)

            ossize_int = int(ossize)

            filename_rom = wanos.wanrommon.get(key)

            version_rom = wanos.wanromver.get(key)

            romsize = wanos.wanrommonossize.get(key)

            romsize_int = int(romsize)

            hash_value_rom = wanos.md5_hash_rom.get(key)

            copy = f"copy http://{source}/ios/{filename} {disk}{filename}"

            copy_rom = f"copy http://{source}/ios/{filename_rom}.bin {disk}{filename_rom}.pkg"

            filename_rom = f'{filename_rom}.pkg'

            # copy = f"copy http://{creds.COPY_CREDS['username']}:{creds.COPY_CREDS['password']}@{source}/{filename} {disk}{filename}"

            break

    if re.search(key, running_image):

        print('Checking for duplicate IOS file...')

        show_dir = connection.send_command(f'dir {disk}', use_textfsm=True)

        for file_dict in show_dir:

            os_ver = file_dict.get('name')

            # print(os_ver)

            if os_ver in filename:

                current_os_ver = filename

            elif running_image in os_ver:

                running_image = os_ver

            elif os_ver in filename_rom:

                new_rom_ver = filename_rom

        do_verify = ''

        flag = 'IOS_ONLY'

        isr4k = False

        firmware_version = ''

        show_rom = ''

        firmware_version = ''

        slot_number = ''

        if 'isr4' in key:

            isr4k = True

            show_rom = connection.send_command('show platform diag', use_textfsm=True)

            pprint(show_rom)

            for rom_dict in show_rom:

                slot_number = rom_dict.get('slot_number')

                if slot_number == 'R0':
                    firmware_version = rom_dict.get('firmware_version')

        if not re.search(filename, current_os_ver) or (
                isr4k and (version_rom not in firmware_version and not re.search(filename_rom, new_rom_ver))):

            print('Checking space...')

            free_size = show_dir[0]['total_free']

            free_size_int = int(free_size)

            print(filename_rom)

            print(new_rom_ver)

            print(version_rom)

            print(firmware_version)

            print(filename)

            print(current_os_ver)

            if isr4k:

                if (not re.search(filename_rom, new_rom_ver) and version_rom not in firmware_version) and not re.search(
                        filename, current_os_ver):

                    ossize_int = ossize_int + romsize_int

                    flag = 'BOTH'

                elif (not re.search(filename_rom, new_rom_ver) and version_rom not in firmware_version):

                    ossize_int = romsize_int

                    flag = 'ROM_ONLY'

            if (free_size_int > ossize_int):

                print('Free Space Exists - Executing Copy Function')

                client_out = connection.send_config_set(client_commands)

                print(client_out)

                if flag == 'BOTH' or flag == 'IOS_ONLY':
                    print(f"Sending copy command {copy}!")

                    out_1 = connection.send_command(copy, expect_string='Destination', cmd_verify=False)

                    print(out_1)

                    out_2 = connection.send_command(filename, expect_string='#', max_loops=172000)

                    print(out_2)

                if flag == 'BOTH' or flag == 'ROM_ONLY':
                    print(f"Sending copy command {copy_rom}!")

                    out_3 = connection.send_command(copy_rom, expect_string='Destination', cmd_verify=False)

                    print(out_3)

                    out_4 = connection.send_command(filename_rom, expect_string='#', max_loops=172000)

                    print(out_4)

                no_client_out = connection.send_config_set(no_client_commands)

                print(no_client_out)

                show_dir = connection.send_command(f'dir {disk}', use_textfsm=True)

                new_os_ver = ''

                new_rom_size = ''

                for i in show_dir:

                    os_ver = i.get('name')

                    if os_ver == filename:

                        new_os_ver = os_ver

                        new_os_size = i.get('size')

                    elif isr4k and os_ver == filename_rom:

                        new_rom_ver = os_ver

                        new_rom_size = i.get('size')

                if new_os_ver == '':

                    print('****FAILED TO TRANSFER*****\n\tPlease check the HTTP server\n\t')

                    return host_name, f"****FAILED TO TRANSFER (verify http server connection)*****{host_name}"

                elif new_os_size != ossize:

                    print('****IOS FAILED TO TRANSFER CORRECTLY*****\n\tPlease check the HTTP server directory\n\t')

                    return host_name, f"****FAILED TO TRANSFER CORRECTLY (verify http server directory)*****{host_name}"

                elif (flag == 'BOTH' or flag == 'ROM_ONLY') and new_rom_size != romsize:

                    print('****ROM FAILED TO TRANSFER CORRECTLY*****\n\tPlease check the HTTP server directory\n\t')

                    return host_name, f"****ROM FAILED TO TRANSFER CORRECTLY (verify http server directory)*****{host_name}"

                else:

                    if flag == 'BOTH' or flag == 'IOS_ONLY':
                        print(f'\nVerifying image on {host_name}\n')

                        do_verify = connection.send_command(

                            # Appox 12 Min for 400Meg => 2700 loops= 1 min

                            f'verify /md5 {disk}{filename} {hash_value}', max_loops=50000)

                        print(do_verify)

                    if flag == 'BOTH' or flag == 'ROM_ONLY':
                        do_verify_rom = connection.send_command(

                            f'verify /md5 {disk}{filename_rom}', max_loops=50000)

                        print(do_verify_rom)

                if (flag == 'BOTH' or flag == 'ROM_ONLY') and not re.search(hash_value_rom, do_verify_rom):

                    return host_name, 'ROMMON MD5 hash verification ERROR. Please verify copied ROMMON Package'



                elif re.search(hash_value, do_verify):

                    show_boot = connection.send_command('show run | i boot system')

                    no_boot_commands = []

                    if show_boot != '':

                        boot_raw = ttp(data=show_boot, template=ttp_template_boot_system)

                        boot_raw.parse()

                        test_var = boot_raw.result(format='raw')[0][0]

                        dict_var = {}

                        if type(test_var) == type(dict_var):

                            boot_system = boot_raw.result(format='raw')[0]

                        else:

                            boot_system = boot_raw.result(format='raw')[0][0]

                        x = 0

                        while x < len(boot_system):
                            boot_image = boot_system[x]['boot_IOS']

                            no_boot_commands = no_boot_commands + [f'no boot system {boot_image}']

                            x = x + 1

                    boot_commands = [f'boot system flash {disk}{filename}', f'boot system flash {disk}{running_image}']

                    if no_boot_commands != []:
                        no_boot_out = connection.send_config_set(no_boot_commands)

                    boot_out = connection.send_config_set(boot_commands)

                    connection.fast_cli = False

                    save_out = connection.save_config()

                    connection.fast_cli = True

                    print(save_out)

                    print(f'Image {filename} on {host_name} complete\n')

                    with open(f"C:/SFTP_Root/script_logs/image_copy_details_{username}.txt", "a") as a:

                        a.write(f'\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@** {host_name} **@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

                        a.write(client_out)

                        a.write(out_1)

                        a.write(out_2)

                        a.write(do_verify)

                        if flag == 'BOTH':
                            a.write(out_3)

                            a.write(out_4)

                            a.write(do_verify_rom)

                        a.write(no_client_out)

                        a.write(no_boot_out)

                        a.write(boot_out)

                        a.write(save_out)

                        a.write('\n\n\n')

                    if flag == 'BOTH':

                        return host_name, f'completed both IOS and ROM --> {filename} and {filename_rom}'

                    else:

                        return host_name, f'complete IOS --> {filename}'



                elif flag == 'BOTH' or flag == 'IOS_ONLY':

                    return host_name, 'MD5 hash verification ERROR. Please verify copied image'

                else:

                    connection.fast_cli = False

                    save_out = connection.save_config()

                    connection.fast_cli = True

                    with open(f"C:/SFTP_Root/script_logs/image_copy_details_{username}.txt", "a") as a:

                        a.write(f'\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@** {host_name} **@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

                        a.write(out_3)

                        a.write(out_4)

                        a.write(do_verify_rom)

                        a.write(save_out)

                        a.write('\n\n\n')

                    return host_name, f'complete ROM --> {filename_rom}'



            else:

                return host_name, f"Not enough space, free space = {free_size_int} space needed = {ossize_int}"

        else:

            return host_name, 'File already exist. No work.'

    else:

        return host_name, 'Wrong Device Version'


# To make this script flexible, it require the user to input arguments variable for scp server, target disk, router model type, image name.

if __name__ == '__main__':

    router = input('Please enter the IP address of the router (destination of the http copy)\n')

    valid_IP = False

    while not valid_IP:

        var = re.search(r'\d+\.\d+\.\d+\.\d+', router)

        if not var:

            router = input('Please enter a valid IP address of the router\n')

        else:

            valid_IP = True

    username = getlogin()

    with open(f"C:\\SFTP_Root\\script_logs\\image_copy_{username}.log", "w+") as a:

        a.write(timestamp)

        a.write('\n')

    with open(f"C:\\SFTP_Root\\script_logs\\image_copy_details_{username}.txt", "w+") as b:

        b.write(timestamp)

    http_server = input('Please enter the HTTP server address or press enter to accept 1.1.1.1:\n')

    server_check = re.search(r'\d+\.\d+\.\d+\.\d+', http_server)

    if not server_check:

        http_server = ‘1.1
        .1
        .1’



        interface = input('\nPlease enter the download interface or press enter for Gig0\n')

        if interface == '':
            interface = 'Gig0'

        authentication = 'TACACS maintenance acccount'

        auth_method = input(
            '\nIs this router authenticating via the local account "cisco"\n"Y or N"\nAnything other than "Y" will assume TACACS authentication\n')

        if auth_method == 'Y':

            auth_method = 'ESL_WAN1'

            authentication = 'cisco local user'

        else:

            auth_method = 'ESL_WAN'

        list_of_commands = [(router, interface, http_server, auth_method)]

        print(
            f"You are about to pull the IOS image using http from:\n {http_server} to {router} on interface {interface} authenticating via {authentication}")

        response = input("\nDo You Wish To Continue? [Y/N] ")

        if response.upper() != "Y":
            exit(0)

        with ThreadPool(1) as p:

            if False:
                assert isinstance(p, ThreadPool)

            for idx, res in enumerate(p.imap_unordered(sendCopy, list_of_commands)):
                print(res)

                with open(f'C:\\SFTP_Root\\script_logs\\image_copy_{username}.log', 'a') as f:
                    f.write(str(res))

                    f.write('\n')



