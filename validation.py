# TOO MUCH INDENTATION!!!
def do_a_thing(age, limit, name):
    if age is not None:
        if isinstance(age, int):
            if age >= 21:
                if limit is not None:
                    if isinstance(limit, int):
                        if limit > 0:
                            # MEAT OF THE FUNCTION 300 line
                            print("Doing the thing!!")
                        else:
                            print("Error: ...")
                            return False
                    else:
                        print("Error: ...")
                        return False
                else:
                    print("Error: ...")
                    return False
            else:
                print("Error: ...")
                return False
        else:
            print("Error: ...")
            return False
    else:
        print("Error: ...")
        return False
    return True


# ALTERNATIVE INVERT AND SEPARATE

def parameters_are_valid(age, limit, name):
    if age is None:
        print("Error: ...")
        return False
    if not isinstance(age, int):
        print("Error: ...")
        return False
    if not age >= 21:
        print("Error: ...")
        return False
    if limit is None:
        print("Error: ...")
        return False
    if not isinstance(limit, int):
        print("Error: ...")
        return False
    if limit > 0:
        print("Error: ...")
        return False
    return True


def do_a_thing(age, limit, name):
    if not parameters_are_valid(age, limit, name):
        print("ERROR")
        return False
    # MEAT OF THE FUNCTION 300 line
    print("Doing the thing!!")

    return True
