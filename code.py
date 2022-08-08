# sysinfo.py http://mew.cx/  2022-07-24
# SPDX

import board
import microcontroller as soc
import os
import sys

__version__ = "0.0.0.0"
__repo__    = "todo"

# functions #################################################################

def Hexify(data):
    "Return a bytearray's hexadecimal ASCII text"
    #return "".join("%02x" % i for i in data)
    return "".join("{:02x}".format(i) for i in data)

def PinMap():
    """Derived from:
    https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/CircuitPython_Essentials/Pin_Map_Script
    """
    pinlist = []
    for spin in dir(soc.pin):
        pin_attr = getattr(soc.pin, spin)
        if isinstance(pin_attr, soc.Pin):
            pins = ["soc.{}".format(spin)]
            for bpin in dir(board):
                if getattr(board, bpin) is pin_attr:
                    pins.append("board.{}".format(bpin))
            pinlist.append("\t".join(pins))
    return sorted(pinlist)

def FsInfo(statvfs_info):
    """Return filesystem capacity and availability in bytes.
    https://docs.circuitpython.org/en/latest/shared-bindings/os/#os.statvfs
    """
    f_bsize, f_frsize, f_blocks, f_bfree, f_bavail = statvfs_info
    #assert(f_bsize == f_frsize)
    #assert(f_bfree == f_bavail)
    #assert(f_ffree == f_favail)
    sizeof_full = f_blocks * f_frsize
    sizeof_free = f_bfree * f_frsize
    return (sizeof_full, sizeof_free)

#############################################################################

def main(out):
    out.write("board.board_id : {}\n".format(board.board_id))
    out.write("uid : {}\n".format(Hexify(soc.cpu.uid)))

    try:
        cpus = soc.cpus
        #assert(cpus[0].uid == cpus[1].uid)
        out.write("len(cpus) : {} (".format(len(cpus)))
        out.write(" ".join("{}".format(Hexify(cpu.uid)) for cpu in cpus))
        out.write(")\n")
    except:
        pass

    out.write("sys.implementation : {}\n".format(sys.implementation))
    out.write("sys.path : {}\n".format(sys.path))
    out.write("sys.platform : {}\n".format(sys.platform))
    out.write("sys.version_info : {}\n".format(sys.version_info))
    out.write("os.uname() : {}\n".format(os.uname()))

    statvfs_info = os.statvfs('/')
    sizeof_full, sizeof_free = FsInfo(statvfs_info)
    out.write("os.statvfs('/') : {} {} of {} ({}\%) free\n".format(
        statvfs_info, sizeof_free, sizeof_full,
        100.0 * sizeof_free / sizeof_full)

    if soc.nvm:
        out.write("len(nvm) : {}".format(len(soc.nvm)))
        #out.write(" ({})\n".format(Hexify(soc.nvm)))
        out.write("\n")

    out.write("\n")
    out.write("dir(microcontroller.pin) :\n{}\n".format(dir(soc.pin)))
    out.write("\n")
    out.write("dir(board) :\n{}\n".format(dir(board)))
    out.write("\n")
    try:
        import wifi
        # TODO print stuff
    except:
        pass

    out.write("PinMap() {\n")
    for i in PinMap():
        out.write("{}\n".format(i))
    out.write("}\n")

    out.write("help('modules') {\n")
    help('modules')
    out.write("}\n")

# make it so ################################################################

def Filename():
    return "{}__{}.txt".format(board.board_id, Hexify(soc.cpu.uid))

with open(Filename(), "w") as fh:
    main(fh)
os.sync()
soc.reset()

# reference #################################################################
#storage.remount("/", readonly=False) # CPy writable
#storage.remount("/", readonly=True)  # CPy readonly
#print("os.stat foo", os.stat("/foo.py"))
#out.write("os.stat(/code.py) : {}\n".format(os.stat("/code.py")))
#out.write("os.sep : {}\n".format(os.sep))
#print("os.getcwd", os.getcwd())
#with open("/tmp.txt", "a") as fp:
#    fp.write("hello, world!")
#os.rename("/boot.py", "/boot.bak")
#out.write("sys.version : {}\n".format(sys.version))
#out.write("sys.modules : {}\n".format(sys.modules))

# eof
