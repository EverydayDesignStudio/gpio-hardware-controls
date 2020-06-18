#!/usr/bin/env python3

import threading
import time

num = 10

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            # print('Doing something imporant in the background')
            global num
            num = num + 1
            time.sleep(self.interval)

example = ThreadingExample()
while True:
    print(num)
    time.sleep(0.1)

# time.sleep(3)
# print('Checkpoint')
# global num
# print(num)
# time.sleep(2)
# print('Bye')
