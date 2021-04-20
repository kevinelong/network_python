while True:  # START THE "INFINITE" LOOP
    text = input("ENTER COMMAND:")
    text = text.upper()

    # if text == "QUIT" or text == "Q" or text == "X" or text == "EXIT":
    #     break

    if text in ["QUIT", "Q", "X", "EXIT"]:
        break  # EXIT THE INFINITE LOOP

print("ALL DONE")
