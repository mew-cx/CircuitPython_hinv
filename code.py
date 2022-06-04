# uname/code.py

print("\nsysinfo ==================")

import board
print("\nboard.board_id :", board.board_id)
print("\ndir(board) :", dir(board))

import os
#print("\ndir(os) :", dir(os))
print("\nos.uname() :", os.uname())

import supervisor
#print("\ndir(supervisor) :", dir(supervisor))

import microcontroller
print("\ndir(microcontroller) :", dir(microcontroller))
print("\ndir(microcontroller.pin) :", dir(microcontroller.pin))

import sys
print("\ndir(sys) :", dir(sys))

import micropython
print("\ndir(micropython) :", dir(micropython))

print("\nhelp('modules') {")
help('modules')
print("}")

print("==========================")
