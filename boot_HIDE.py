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

print("".join("%02x" % i for i in microcontroller.cpu.uid))
print("".join("{:02x}".format(i) for i in microcontroller.cpu.uid))

print("getcwd", os.getcwd())

#storage.remount("/", readonly=False) # CPy writable
#storage.remount("/", readonly=True)  # CPy readonly

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


#############################################################################


# uname/code.py

print("\nsysinfo ==================")

import board
print("board.board_id :", board.board_id)
print("dir(board) :", dir(board))

import os
#print("\ndir(os) :", dir(os))
print("os.uname() :", os.uname())

import supervisor
#print("\ndir(supervisor) :", dir(supervisor))

import microcontroller
print("\ndir(microcontroller) :", dir(microcontroller))
print("dir(microcontroller.pin) :", dir(microcontroller.pin))

import sys
print("\ndir(sys) :", dir(sys))
print("sys.version :", sys.version)
print("sys.platform :", sys.platform)
print("sys.implementation :", sys.implementation)
print("sys.path :", sys.path)
#print("sys.modules :", sys.modules)

import micropython
#print("\ndir(micropython) :", dir(micropython))

print("\nhelp('modules') {")
help('modules')
print("}")

import pin_map
print("==========================")

#############################################################################

"""CircuitPython Essentials Pin Map Script"""
import microcontroller
import board

board_pins = []
for pin in dir(microcontroller.pin):
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append("board.{}".format(alias))
        if len(pins) > 0:
            board_pins.append(" ".join(pins))
for pins in sorted(board_pins):
    print(pins)

#############################################################################

__future__        adafruit_hid/mouse                  microcontroller   supervisor
__main__          adafruit_pixelbuf micropython       sys
adafruit_hid/__init__               array             neopixel          time
adafruit_hid/consumer_control       board             neopixel_write    touchio
adafruit_hid/consumer_control_code  builtins          os                usb_cdc
adafruit_hid/keyboard               collections       rainbowio         usb_hid
adafruit_hid/keyboard_layout_base   digitalio         random            usb_midi
adafruit_hid/keyboard_layout_us     gc                storage
adafruit_hid/keycode                math              struct
Plus any modules on the filesystem

os.uname() :  (sysname='samd21', nodename='samd21', release='7.2.5', version='7.2.5 on 2022-04-06', machine='Adafruit NeoPixel Trinkey M0 with samd21e18')

dir(board) :  ['__name__', 'NEOPIXEL', 'TOUCH1', 'TOUCH2', 'board_id']

board.board_id :  neopixel_trinkey_m0

dir(microcontroller) :  ['__name__', 'Pin', 'Processor', 'ResetReason', 'RunMode', 'cpu', 'delay_us', 'disable_interrupts', 'enable_interrupts', 'nvm', 'on_next_reset', 'pin', 'reset', 'watchdog']

dir(microcontroller.pin) :  ['PA03', 'PA05', 'PA07', 'PA22', 'PA23']

#############################################################################

board.board_id : raspberry_pi_pico
dir(board) : ['__class__', '__name__', 'A0', 'A1', 'A2', 'A3', 'GP0', 'GP1', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP2', 'GP20', 'GP21', 'GP22', 'GP23', 'GP24', 'GP25', 'GP26', 'GP26_A0', 'GP27', 'GP27_A1', 'GP28', 'GP28_A2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'LED', 'SMPS_MODE', 'VBUS_SENSE', 'VOLTAGE_MONITOR', 'board_id']
os.uname() : (sysname='rp2040', nodename='rp2040', release='7.3.0', version='7.3.0 on 2022-05-23', machine='Raspberry Pi Pico with rp2040')

dir(microcontroller) : ['__class__', '__name__', 'Pin', 'Processor', 'ResetReason', 'RunMode', 'cpu', 'cpus', 'delay_us', 'disable_interrupts', 'enable_interrupts', 'nvm', 'on_next_reset', 'pin', 'reset', 'watchdog']
dir(microcontroller.pin) : ['__class__', 'GPIO0', 'GPIO1', 'GPIO10', 'GPIO11', 'GPIO12', 'GPIO13', 'GPIO14', 'GPIO15', 'GPIO16', 'GPIO17', 'GPIO18', 'GPIO19', 'GPIO2', 'GPIO20', 'GPIO21', 'GPIO22', 'GPIO23', 'GPIO24', 'GPIO25', 'GPIO26', 'GPIO27', 'GPIO28', 'GPIO29', 'GPIO3', 'GPIO4', 'GPIO5', 'GPIO6', 'GPIO7', 'GPIO8', 'GPIO9']

dir(sys) : ['__class__', '__name__', 'argv', 'byteorder', 'exit', 'implementation', 'maxsize', 'modules', 'path', 'platform', 'stderr', 'stdin', 'stdout', 'version', 'version_info']
sys.version : 3.4.0
sys.platform : RP2040
sys.implementation : (name='circuitpython', version=(7, 3, 0), mpy=517)
sys.path : ['', '/', '/lib']

help('modules') {
__future__        board             onewireio         touchio
__main__          builtins          os                traceback
_asyncio          busio             paralleldisplay   ulab
_bleio            collections       pulseio           ulab
_eve              countio           pwmio             ulab.fft
adafruit_bus_device                 digitalio         qrio              ulab.linalg
adafruit_bus_device.i2c_device      displayio         rainbowio         ulab.numpy
adafruit_bus_device.spi_device      errno             random            ulab.scipy
adafruit_pixelbuf floppyio          re                ulab.scipy.linalg
aesio             fontio            rgbmatrix         ulab.scipy.optimize
alarm             framebufferio     rotaryio          ulab.scipy.signal
analogio          gc                rp2pio            ulab.scipy.special
array             getpass           rtc               ulab.utils
atexit            gifio             sdcardio          usb_cdc
audiobusio        imagecapture      select            usb_hid
audiocore         io                sharpdisplay      usb_midi
audiomixer        json              storage           uselect
audiomp3          keypad            struct            vectorio
audiopwmio        math              supervisor        watchdog
binascii          microcontroller   synthio           zlib
bitbangio         micropython       sys
bitmaptools       msgpack           terminalio
bitops            neopixel_write    time
Plus any modules on the filesystem
}
board.A0 board.GP26 board.GP26_A0
board.A1 board.GP27 board.GP27_A1
board.A2 board.GP28 board.GP28_A2
board.A3 board.VOLTAGE_MONITOR
board.GP0
board.GP1
board.GP10
board.GP11
board.GP12
board.GP13
board.GP14
board.GP15
board.GP16
board.GP17
board.GP18
board.GP19
board.GP2
board.GP20
board.GP21
board.GP22
board.GP23 board.SMPS_MODE
board.GP24 board.VBUS_SENSE
board.GP25 board.LED
board.GP3
board.GP4
board.GP5
board.GP6
board.GP7
board.GP8
board.GP9
