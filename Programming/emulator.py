import os
clear = lambda: os.system('cls')

def load_rom(file, start_address=0x00):
    print('Loading {0}...'.format(file))
    print('Writing to address {0:x04}'.format(start_address))

while True:
    try:
        cmd, *args = input('$').split()
        if cmd in ['clr', 'clear']: clear()
        if cmd in ['q', 'quit', 'exit']: break
        if cmd == 'load': load_rom(args[0], args[1])
    except Exception as e:
        print(str(e))



        
input('Emulator terminated. Press [ENTER] to exit.')