from threading import Thread
import time


def timer(name, delay, repeat):
    print("Timer: " + name + " Started")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + " Completed")


t1 = Thread(target=timer, args=("Timer1", 1, 5))
t2 = Thread(target=timer, args=("Timer2", 2, 5))

t1.start()
t2.start()


print("Main complete")

t1.join()
t2.join()
print("Waited until thread was complete")

