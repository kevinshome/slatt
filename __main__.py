#slatt development release 001

#imports
import sys
import os

#set slatt filename to var
slatt_file = sys.argv[1]

#get line list
with open(slatt_file) as slatt:
    lineList = slatt.readlines()

#parse slatt file
with open(slatt_file) as slatt:
    for num, line in enumerate(slatt, 1):
        #search for "ok!" at end of file
        if lineList[len(lineList) - 1].split()[0] != "ok!" or num == 1 and "**slatt!**" not in line:
            if lineList[len(lineList) - 1].split()[0] != "ok!":
                print('Error in {0}: Non-valid slatt file (error 1: require "ok!" on last line of program file)'.format(slatt_file))
                #search for "*slatt!*" at beginning of file
            if line.split()[0] != "**slatt!**":
                print('Error in {0}: Non-valid slatt file (error 2: require "**slatt!**" on line 1 of program file)'.format(slatt_file))

            sys.exit()
        #prints if "+yo pierre()" is in the line
        if "+yo pierre(" in line:
            pline = line
            pline = pline.replace("+yo pierre", "print")
            os.system("echo '{0}' >> /tmp/hello.py".format(pline))

os.system("python /tmp/hello.py")
os.remove("/tmp/hello.py")
