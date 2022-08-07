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

def Filename():
    return "{}__{}.txt".format(board.board_id, Hexify(soc.cpu.uid))

def PinMap():
    """CircuitPython Essentials Pin Map Script"""
    uc_pins = []
    for ucpin in dir(soc.pin):
        uc_attr = getattr(soc.pin, ucpin)
        if isinstance(uc_attr, soc.Pin):
            b_pins = [ucpin]
            for bpin in dir(board):
                if getattr(board, bpin) is uc_attr:
                    b_pins.append("board.{}".format(bpin))
            if len(b_pins) > 1:
                uc_pins.append("\t".join(b_pins))
    return sorted(uc_pins)

def VfsInfo(statvfs_info):


f_bsize,
f_frsize,
f_blocks,
f_bfree,
f_bavail,
f_files,
f_ffree,
f_favail,
f_flag,
f_namemax


f_bsize – file system block size
f_frsize – fragment size
f_blocks – size of fs in f_frsize units
f_bfree – number of free blocks
f_bavail – number of free blocks for unprivileged users
f_files – number of inodes
f_ffree – number of free inodes
f_favail – number of free inodes for unprivileged users
f_flag – mount flags
f_namemax – maximum filename length


#############################################################################

def main(out):
    out.write("board.board_id : {}\n".format(board.board_id))
    out.write("uid : {}\n".format(Hexify(soc.cpu.uid)))

    try:
        cpus = soc.cpus
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
    out.write("os.statvfs(/) : {}\n".format(os.statvfs("/")))
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
https://docs.circuitpython.org/en/latest/shared-bindings/os/#os.statvfs

os.statvfs(path: str) → Tuple[int, int, int, int, int, int, int, int, int, int]
Get the status of a filesystem.
Returns a tuple with the filesystem information in the following order:

f_bsize – file system block size
f_frsize – fragment size
f_blocks – size of fs in f_frsize units
f_bfree – number of free blocks
f_bavail – number of free blocks for unprivileged users
f_files – number of inodes
f_ffree – number of free inodes
f_favail – number of free inodes for unprivileged users
f_flag – mount flags
f_namemax – maximum filename length

Parameters related to inodes: f_files, f_ffree, f_avail and the f_flags
parameter may return 0 as they can be unavailable in a port-specific
implementation.
