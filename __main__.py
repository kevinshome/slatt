#slatt development release

#MIT License
#
#Copyright (c) 2019 kevinshome
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#imports
import sys
import os

#set slatt filename to var
global slatt_file
global line
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
        else:
            #look, obviously the program doesn't *actually* need these in it
            #it's just an aesthetic thing okay
            #get off my fucking case, mom. god.
            line = line.replace("**slatt!**", "")
            line = line.replace("ok!", "")

        #function to parse slatt file and compile to python
        def parse():
            global slatt_file
            global line
            #prints if "+yo pierre()" is in the line
            slatt_file = slatt_file.replace("/", "")
            if "+yo pierre(" in line:
                line = line.replace("+yo pierre", "print")
                parse()
            #set variables using "^wholelotta>"
            elif "^wholelotta>" in line:
                line = line.replace("^wholelotta>", "=")
                parse()
            #is equal to (==)
            elif "^iswholelotta>" in line:
                line = line.replace("^iswholelotta>", "==")
                parse()
            #define functions using "_flex*"
            elif "_flex*" in line:
                line = line.replace("_flex*", "def ")
                parse()
            #call function
            elif "_imightcall" in line:
                line = line.replace("_imightcall ", "")
                parse()
            #if/else statement
            elif "*!yah" in line:
                line = line.replace("*!yah", "if")
                parse()
            elif "*!nah" in line:
                line = line.replace("*!nah", "else")
                parse()
            #input statement
            elif "wokeuplike*(" in line:
                line = line.replace("wokeuplike*", "input")
                parse()
            else:
                os.system("echo '{0}' >> /tmp/{1}.py".format(line, slatt_file))
        parse()

#i know this is such a cheap fucking way to do this
#but like, i'm a shitty programmer
#i'm sorry :(
os.system("python /tmp/{0}.py".format(slatt_file))
os.remove("/tmp/{0}.py".format(slatt_file))
