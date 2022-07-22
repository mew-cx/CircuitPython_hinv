# sysinfo.py

import storage
import os
import microcontroller
import sys
import supervisor
import board
import errno
import micropython

def Filename():
    #print("uidX", "".join("%02x" % i for i in microcontroller.cpu.uid))
    #print("uidY", "".join("{:02x}".format(i) for i in microcontroller.cpu.uid))
    uid = "".join("{:02x}".format(i) for i in microcontroller.cpu.uid)
    return "{}__{}.txt".format(board.board_id, uid)

def PinMap():
    """CircuitPython Essentials Pin Map Script"""
    board_pins = []
    for ucpin in dir(microcontroller.pin):
        if isinstance(getattr(microcontroller.pin, ucpin), microcontroller.Pin):
            pins = [ucpin]
            for alias in dir(board):
                if getattr(board, alias) is getattr(microcontroller.pin, ucpin):
                    pins.append("board.{}".format(alias))

            if len(pins) > 0:
                board_pins.append("\t".join(pins))

    for pins in sorted(board_pins):
        print(pins)

#############################################################################

print("Filename() : ", Filename())

print("board.board_id : ", board.board_id)
print("sys.implementation : ", sys.implementation)
print("sys.modules : ", sys.modules)
print("sys.path : ", sys.path)
print("sys.platform : ", sys.platform)
print("sys.version : ", sys.version)
print("sys.version_info : ", sys.version_info)
print("os.uname() :", os.uname())

#supervisor.set_rgb_status_brightness(100)

print("uid : ", repr(microcontroller.cpu.uid))
#print("uid0 : ", microcontroller.cpus[0].uid)
#print("uid1 : ", microcontroller.cpus[1].uid)

print("statvfs / : ", os.statvfs("/"))
print("stat /code.py : ", os.stat("/code.py"))
print("sep : ", os.sep)

#storage.remount("/", readonly=False) # CPy writable
#storage.remount("/", readonly=True)  # CPy readonly
#print("stat foo", os.stat("/foo.py"))
#print("getcwd", os.getcwd())
#with open("/tmp.txt", "a") as fp:
#    fp.write("hello, world!")
#os.rename("/boot.py", "/boot.bak")

#############################################################################
# uname/code.py

print("\ndir(microcontroller.pin) :", dir(microcontroller.pin))

print("\ndir(board) :", dir(board))
print("\ndir(os) :", dir(os))
print("\ndir(sys) :", dir(sys))
print("\ndir(storage) :", dir(storage))
print("\ndir(errno) :", dir(errno))
print("\ndir(micropython) :", dir(micropython))
print("\ndir(microcontroller) :", dir(microcontroller))
print("\ndir(supervisor) :", dir(supervisor))

print("\nhelp('modules') {")
#help('modules')
print("}")

print("\nPinMap() {")
PinMap()
print("}")

os.sync()
print("done =====================")
#microcontroller.reset()
