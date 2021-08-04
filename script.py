import frida, sys, time, os, json
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("pkg",
                    help="Package name to attach")
parser.add_argument("cls",
                    help="Class name to attach Frida")
parser.add_argument("mth",
                    help="Method name to call in Frida")
parser.add_argument("file", default="arguments.txt", nargs='?',
                     help="File name in this folder where the arguments to the method are stored (default name: arguments.txt).")
parser.add_argument('-s', '--stdin', action="store_true",
                    help='Read from stdin INSTEAD of the file.')


args = parser.parse_args()


def from_stdin(): 
    script.on('message', on_message)
    script.load()
    for line in sys.stdin:
        script.post({'type': 'cls', 'class': args.cls, 'meth': args.mth, 'line':line})
        time.sleep(1)  # fails without this sleep
        device.resume(pid)
        sys.stdin.read()
  

def from_file():
    count = 0
    my_input = [ ]
    with open("arguments.txt") as fp:
        while True:
            count += 1
            line = fp.readline()
            if not line:
                break
            my_input.append(line)
    script.on('message', on_message)
    script.load()
    script.post({'type': 'cls', 'class': args.cls, 'meth': args.mth, 'line':my_input})
    time.sleep(1)  # fails without this sleep
    device.resume(pid)
    sys.stdin.read()


device = frida.get_usb_device()
pid = device.spawn([args.pkg])
session = device.attach(pid)

def on_message(message, data):
    print(message["payload"])


if args.stdin:
    with open('stdin.js') as f:
        print("Wait for the APP to open and monitor if it crashes!! Then you can paste the lines :D")
        script = session.create_script(f.read())
        from_stdin()
else:
    with open('file.js') as f:
        script = session.create_script(f.read())
        from_file()  
