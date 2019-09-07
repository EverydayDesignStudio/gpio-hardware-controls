import RPi.GPIO as gpio

val = None;
pin = None;
state = None;
gpio.setmode(gpio.BCM)

# gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_DOWN)
# gpio.output(12, gpio.HIGH)
# gpio.output(12, gpio.LOW)

while(True):
    try:
        val = input("Enter GPIO number [0, 27] or set the current GPIO to [h | high] or [l | low]: ")
        if (val.isdigit()):
            # Print the ADC values.
            print("\nCurrent GPIO: {}, state: {}\n".format(pin, state))
            pin_no = int(val)
            if (pin_no >= 0 and pin_no <= 27):
                if (pin is not None):
                    print("@@@@ Switching GPIO {} -> {}".format(pin, pin_no))

                pin = pin_no

                gpio.setup(pin, gpio.OUT)
                print("@@ GPIO {} is now set to OUT\n".format(pin))

            else:
                print("\n!!!! Value error; out of range. [0, 27]\n")
        else:
            if (pin is not None and (val == 'high' or val == 'h')):
                state = 'high'
                gpio.output(pin, gpio.HIGH)
                print("\n@@ GPIO {} is now HIGH\n".format(pin))
            elif (pin is not None and (val == 'low' or val == 'l')):
                state = 'low'
                gpio.output(pin, gpio.LOW)
                print("\n@@ GPIO {} is now LOW\n".format(pin))
            else:
                print("\n!!!! Value error! Must enter either 'h' / 'high' for high or 'l' / 'low' for low.\n")

    except KeyboardInterrupt:
        print("@@ Keyboard Interrupt - exiting the test..")
        gpio.cleanup()
        exit();
