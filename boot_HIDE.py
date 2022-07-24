# sysinfo.py http://mew.cx/  2022-07-22
# SPDX

import board
import microcontroller
import storage
import os
import sys

import supervisor
import micropython
import errno

__version__ = "0.0.0.0"
__repo__    = "todo"

# functions #################################################################

def HexifyByteArray(data):
    #return "".join("%02x" % i for i in data)
    return "".join("{:02x}".format(i) for i in data)

def Filename():
    return "{}__{}.txt".format(
        board.board_id,
        HexifyByteArray(microcontroller.cpu.uid))

def PinMap():
    """CircuitPython Essentials Pin Map Script"""
    uc_pins = []
    for ucpin in dir(microcontroller.pin):
        uc_attr = getattr(microcontroller.pin, ucpin)
        if isinstance(uc_attr, microcontroller.Pin):
            b_pins = [ucpin]
            for bpin in dir(board):
                if getattr(board, bpin) is uc_attr:
                    b_pins.append("board.{}".format(bpin))
            if len(b_pins) > 1:
                uc_pins.append("\t".join(b_pins))
    return sorted(uc_pins)

#############################################################################

def main():
    print("Filename() : ", Filename())

    print("board.board_id : ", board.board_id)
    print("uid : ", repr(microcontroller.cpu.uid))
    #print("uid0 : ", microcontroller.cpus[0].uid)
    #print("uid1 : ", microcontroller.cpus[1].uid)

    print("sys.implementation : ", sys.implementation)
    print("sys.modules : ", sys.modules)
    print("sys.path : ", sys.path)
    print("sys.platform : ", sys.platform)
    print("sys.version : ", sys.version)
    print("sys.version_info : ", sys.version_info)
    print("os.uname() :", os.uname())

    print("os.statvfs(/) : ", os.statvfs("/"))
    print("os.stat(/code.py) : ", os.stat("/code.py"))
    print("os.sep : ", os.sep)

    print("\ndir(microcontroller.pin) :", dir(microcontroller.pin))

    print("\ndir(board) :", dir(board))
    print("\ndir(microcontroller) :", dir(microcontroller))
    print("\ndir(storage) :", dir(storage))
    print("\ndir(os) :", dir(os))
    print("\ndir(sys) :", dir(sys))

    print("\ndir(supervisor) :", dir(supervisor))
    print("\ndir(micropython) :", dir(micropython))
    print("\ndir(errno) :", dir(errno))

    print("\nhelp('modules') {")
    help('modules')
    print("}")

    print("\nPinMap() {")
    for i in PinMap():
        print(i)
    print("}")
    print("done =====================")

    os.sync()

# make it so ################################################################

#storage.remount("/", readonly=False) # CPy writable
main()
#storage.remount("/", readonly=True)  # CPy readonly

# future ####################################################################
#microcontroller.reset()
#print("os.stat foo", os.stat("/foo.py"))
#print("os.getcwd", os.getcwd())
#with open("/tmp.txt", "a") as fp:
#    fp.write("hello, world!")
#os.rename("/boot.py", "/boot.bak")
# eof
