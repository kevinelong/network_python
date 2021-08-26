# http://www.pennington.net/py/ciscoconfparse/intro.html
# http://pennington.net/tutorial/ciscoconfparse/ccp_tutorial.html#slide1
# https://github.com/mpenning/ciscoconfparse
# pip install CiscoConfParse
from ciscoconfparse import CiscoConfParse


def parse(file_name):
    f = open(file_name, "r")
    cisco_cfg = CiscoConfParse(f.read().splitlines(keepends=False))

    interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

    # print(interfaces)
    for i in interfaces:
        # print("Interface: {}".format(i.text))
        ip_address = i.re_search_children(r"ip address")[0].text

        description_list = i.re_search_children(r"description")

        if len(description_list) == 0: # HAS DESCRIPTION
            continue

        description = description_list[0].text

        # parts = description.split("-")
        # user = parts[-1]
        if not description.endswith("USER"):
            continue
        authentication_list = i.re_search_children(r"authentication")

        if len(authentication_list) == 1 and authentication_list[0].text == "port-control auto":
            continue

        good_count = 0

        if len(authentication_list) > 0:
            bad = False
            for a in authentication_list:
                if a.text == " authentication open":
                    bad = True
                elif a.text == " authentication port-control auto":
                    good_count += 1
            if bad == False:
                continue
        if good_count > 0 and not bad:
            continue
        #BAD
        print("Interface: {}".format(i.text))
        print("IP Address: {}".format(ip_address))
        print()
    print()

    # print(cisco_cfg)


if __name__ == "__main__":
    parse("./cisco_config_examples/sample01.conf")