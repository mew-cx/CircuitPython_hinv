# SPDX-FileCopyrightText: 2022 Michael Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT
#
# hinv - hardware inventory
# Inspired by the 'hinv' command on Silicon Graphics' IRIX.


import board
import os
import sys
import microcontroller as soc

__version__ = "0.0.1.0"
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
    for mpin in dir(soc.pin):
        pin_attr = getattr(soc.pin, mpin)
        if isinstance(pin_attr, soc.Pin):
            pins = ["microcontroller.{}".format(mpin)]
            for bpin in dir(board):
                if getattr(board, bpin) is pin_attr:
                    pins.append("board.{}".format(bpin))
            pinlist.append("\t".join(pins))
    return sorted(pinlist)

def FsInfo(statvfs_info):
    """Return filesystem capacity and availability in KB.
    https://docs.circuitpython.org/en/latest/shared-bindings/os/#os.statvfs
    """
    f_bsize, f_frsize, f_blocks, f_bfree, f_bavail, _, _, _, _, _ = statvfs_info
    #assert(f_bsize == f_frsize)
    #assert(f_bfree == f_bavail)
    #assert(f_ffree == f_favail)
    KBfull = f_blocks * f_frsize / 1000.0
    KBfree = f_bfree * f_frsize / 1000.0
    return (KBfull, KBfree)

def GenerateResults(out):
    out.write("board.board_id : {}\n".format(board.board_id))
    out.write("uid : {}\n".format(Hexify(soc.cpu.uid)))

    try:
        cpus = soc.cpus
        #assert(cpus[0].uid == cpus[1].uid)
        out.write("len(cpus) : {:d} (".format(len(cpus)))
        out.write(" ".join("{}".format(Hexify(cpu.uid)) for cpu in cpus))
        out.write(")\n")
    except:
        pass

    sys_mpy = sys.implementation.mpy
    out.write("sys.implementation : {} MPY_VERSION={:d} flags=0x{:02x}\n".format(
        sys.implementation, sys_mpy & 0xff, (sys_mpy >> 8) & 0xff))

    out.write("sys.path : {}\n".format(sys.path))
    out.write("sys.platform : {}\n".format(sys.platform))
    out.write("sys.version : {}\n".format(sys.version))
    out.write("os.uname() : {}\n".format(os.uname()))

    statvfs_info = os.statvfs('/')
    KBfull, KBfree = FsInfo(statvfs_info)
    out.write("os.statvfs('/') : {} {:.1f}KB of {:.1f}KB ({:.1f}%) free\n".format(
        statvfs_info, KBfree, KBfull, KBfree / KBfull * 100.0))

    if soc.nvm:
        out.write("len(nvm) : {:d}".format(len(soc.nvm)))
        #out.write(" ({})\n".format(Hexify(soc.nvm)))
        out.write("\n")

    out.write("\n")
    out.write("dir(microcontroller.pin) :\n{}\n\n".format(dir(soc.pin)))
    out.write("dir(board) :\n{}\n\n".format(dir(board)))

    try:
        import wifi
        out.write("dir(wifi) :\n{}\n\n".format(dir(wifi)))
    except:
        pass

    out.write("PinMap() {\n")
    for i in PinMap():
        out.write("{}\n".format(i))
    out.write("}\n")

    out.write("help('modules') {\n")
    help('modules')
    out.write("# TODO how to redirect help('modules') to output filehandle?\n")
    out.write("}\n")

def main():
    try:
        # if flash is writable, send results to file then reboot
        filename = "{}__{}.txt".format(board.board_id, Hexify(soc.cpu.uid))
        with open(filename, "w") as fh:
            GenerateResults(fh)
        os.sync()
        soc.reset()
    except:
        # if flash is read-only, send results to stdout
        GenerateResults(sys.stdout)

# make it so ################################################################

main()

# reference #################################################################
#storage.remount("/", readonly=False) # CPy writable
#storage.remount("/", readonly=True)  # CPy readonly
#os.rename("/boot.py", "/boot.bak")
#print("os.getcwd", os.getcwd())
#print("os.stat code.py", os.stat("/code.py"))
#out.write("sys.version : {}\n".format(sys.version))
#out.write("sys.modules : {}\n".format(sys.modules))
#out.write("os.stat(/code.py) : {}\n".format(os.stat("/code.py")))
#out.write("os.sep : {}\n".format(os.sep))

# eof
