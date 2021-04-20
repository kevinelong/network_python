import re

MINIMUM = 8

RULE = 0
MESSAGE = 1

password_rules = [
    [lambda p: re.compile(r".*[0-9].*").match(p), "Must contain a number."],
    [lambda p: len(p) >= MINIMUM, f"Must be at least {MINIMUM} in length."]
]


def is_password_valid(password):
    message_list = []

    for r in password_rules:
        if not r[RULE](password):
            message_list.append(r[MESSAGE])

    if len(message_list) > 0:  # Show 'em if you got 'em
        print(f"\nERROR: with '{password}':\n\t" + "\n\t".join(message_list))

    return len(message_list) == 0  # True if we have no error messages


# TESTS
if __name__ == "__main__":
    is_password_valid("abc")
    is_password_valid("g11")
    is_password_valid("abcdefgh")

# HOW TO GET MESSAGE FROM ALL EXCEPTIONS
# import sys
# except:  # catch *all* exceptions
# e = sys.exc_info()[0]
