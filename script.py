import frida, sys, time, os, json
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("pkg",
                    help="Package name to attach")
parser.add_argument("cls",
                    help="Class name to attach Frida")
parser.add_argument("mth",
                    help="Method name to call in Frida")
parser.add_argument("file", default="arguments.txt", nargs='?', help="File name in this folder where the arguments to the method are stored.")


args = parser.parse_args()



 
count = 0
my_input = [ ]
with open("arguments.txt") as fp:
    while True:
        count += 1
        line = fp.readline()
 
        if not line:
            break
        my_input.append(line)


device = frida.get_usb_device()
pid = device.spawn([args.pkg])
session = device.attach(pid)


script = session.create_script("""
        var cl;
        var meth;
        var line;
        var strArg = []
        recv('cls', function onMessage(cls) { 
            cl = cls.class;
            meth = cls.meth;
            strArg = cls.line;
        });


        Java.perform(function(){
            for (let i = 0; i < strArg.length; i++) {
                send(
                     Java.use(cl)[meth](strArg[i])
                );
                }
        });

"""
)
def on_message(message, data):
    print(message["payload"])
    
    
script.on('message', on_message)
script.load()
script.post({'type': 'cls', 'class': args.cls, 'meth': args.mth, 'line':my_input})

time.sleep(1)  # fails without this sleep
device.resume(pid)
sys.stdin.read()

