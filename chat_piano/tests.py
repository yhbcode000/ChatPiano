import time

from .tools import *

def myTest():
    print('testing...')
    generate_midi('dummy')
    time.sleep(1)
    print(check_generate_midi_status())
    time.sleep(1)
    print(check_generate_midi_status())

if __name__ == '__main__':
    myTest()
