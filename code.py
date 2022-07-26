# sysinfo.py http://mew.cx/  2022-07-24
# SPDX
# TODO:
# - see 'errno -l' for full list of error codes.
# - use statvfs() to compute storage capacity.
# - put 'try' around 'import wiki' and print of its contents.
# - any reason to keep 'import supervisor'?

import board
import microcontroller
import storage
import os
import sys

import supervisor

__version__ = "0.0.0.0"
__repo__    = "todo"

# functions #################################################################

def Hexify(data):
    "return a bytearray's hexadecimal ASCII text"
    #return "".join("%02x" % i for i in data)
    return "".join("{:02x}".format(i) for i in data)

def Filename():
    return "{}__{}.txt".format(
        board.board_id,
        Hexify(microcontroller.cpu.uid))

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
    out.write("board.board_id : {}\n".format(board.board_id))
    out.write("uid : {}\n".format(Hexify(microcontroller.cpu.uid)))

    try:
        cpus = microcontroller.cpus
        out.write("len(cpus) : {} (".format(len(cpus)))
        out.write(" ".join("{}".format(Hexify(cpu.uid)) for cpu in cpus))
        out.write(")\n")
    except:
        pass

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
