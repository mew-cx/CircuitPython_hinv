# sysinfo.py http://mew.cx/  2022-07-24
# SPDX
# TODO:
# - see 'errno -l' for full list of error codes.
# - put 'try' around 'microcontroller.cpus'
# - use statvfs() to compute storage capacity.

import board
import microcontroller
import storage
import os
import sys

import supervisor
import micropython

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

def main(out):
    out.write("Filename() : {}\n".format(Filename()))

    out.write("board.board_id : {}\n".format(board.board_id))
    out.write("uid : {}\n".format(HexifyByteArray(microcontroller.cpu.uid)))

    #out.write("len(cpus) : {}\n".format(len(microcontroller.cpus)))
    #for cpu in microcontroller.cpus:
    #    print("cpu :", HexifyByteArray(cpu.uid))

    out.write("sys.implementation : {}\n".format(sys.implementation))
    out.write("sys.modules : {}\n".format(sys.modules))
    out.write("sys.path : {}\n".format(sys.path))
    out.write("sys.platform : {}\n".format(sys.platform))
    out.write("sys.version : {}\n".format(sys.version))
    out.write("sys.version_info : {}\n".format(sys.version_info))
    out.write("os.uname() : {}\n".format(os.uname()))

    out.write("os.statvfs(/) : {}\n".format(os.statvfs("/")))
    out.write("os.stat(/code.py) : {}\n".format(os.stat("/code.py")))
    out.write("os.sep : {}\n".format(os.sep))
    out.write("\n")

    out.write("dir(microcontroller.pin) :\n{}\n\n".format(dir(microcontroller.pin)))

    out.write("dir(board) :\n{}\n\n".format(dir(board)))
    out.write("dir(microcontroller) :\n{}\n\n".format(dir(microcontroller)))
    out.write("dir(storage) :\n{}\n\n".format(dir(storage)))
    out.write("dir(os) :\n{}\n\n".format(dir(os)))
    out.write("dir(sys) :\n{}\n\n".format(dir(sys)))

    out.write("dir(supervisor) :\n{}\n\n".format(dir(supervisor)))
    out.write("dir(micropython) :\n{}\n\n".format(dir(micropython)))
    out.write("\n")

    out.write("PinMap() {\n")
    for i in PinMap():
        out.write("{}\n".format(i))
    out.write("}\n")

    out.write("help('modules') {\n")
    help('modules')
    out.write("}\n")

# make it so ################################################################

with open(Filename(), "w") as f:
    main(f)
os.sync()
microcontroller.reset()

# future ####################################################################
#storage.remount("/", readonly=False) # CPy writable
#storage.remount("/", readonly=True)  # CPy readonly
#print("os.stat foo", os.stat("/foo.py"))
#print("os.getcwd", os.getcwd())
#with open("/tmp.txt", "a") as fp:
#    fp.write("hello, world!")
#os.rename("/boot.py", "/boot.bak")
# eof
