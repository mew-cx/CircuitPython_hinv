import storage
import os
import microcontroller
import sys
import supervisor
import board
#import errno

print("board_id", board.board_id)
print(sys.implementation)
print(sys.modules)
print(sys.path)
print(sys.platform)
print(sys.version)
print(sys.version_info)

supervisor.set_rgb_status_brightness(100)

#print("errorcode", errno.errcode)

print("uname", os.uname())
print("uid", repr(microcontroller.cpu.uid))
#print("uid0", microcontroller.cpus[0].uid)
#print("uid1", microcontroller.cpus[1].uid)
print("getcwd", os.getcwd())

#storage.remount("/", False)

#print("mkdir", os.mkdir("/a"))
#print("mkdir", os.mkdir("/a"))
#print("remove", os.remove("/nothing"))

print("listdir /", os.listdir("/"))

print("statvfs /", os.statvfs("/"))
print("stat code.py", os.stat("/code.py"))
#print("stat foo", os.stat("/foo.py"))

print("sep", os.sep)

#with open("/tmp.txt", "a") as fp:
#    fp.write("hello, world!")

#os.rename("/boot.py", "/boot.bak")

os.sync()
os.sync()

print("all done")
#microcontroller.reset()
