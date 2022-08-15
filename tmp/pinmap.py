import board
import microcontroller as soc

def PinMap():
    pinlist = []
    for mpin in dir(soc.pin):

        pin_attr = getattr(soc.pin, mpin)
        print("\tgetattr(", soc.pin, ",", mpin, ") =", pin_attr)
        x = isinstance(pin_attr, soc.Pin)
        print("\tisinstance(", pin_attr, ",", soc.Pin, ") =", x)

        if x:
            pins = ["microcontroller.{}".format(mpin)]
            for bpin in dir(board):

                y = getattr(board, bpin)
                print("\t\tgetattr(", board, ",", bpin, ") =", y)
                z = y is pin_attr
                print("\t\t", y, "is", pin_attr, "=", z)

                if z:
                    pins.append("board.{}".format(bpin))
            pinlist.append("\t".join(pins))
    return sorted(pinlist)

print("dir(soc.pin)", dir(soc.pin))
print("dir(board) ", dir(board))
for i in PinMap():
    print(i)
