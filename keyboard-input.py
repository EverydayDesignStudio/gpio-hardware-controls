#!/usr/bin/env python3

import getch


def main():
    print('Starting Keyboard Input program')

    while True:
        # print('\n')
        keycode = ord(getch.getch())
        print('Keycode is: {kc}'.format(kc=keycode))
        # print(getch.getch())


if __name__ == "__main__":
    main()
