#!/usr/bin/python

###########################################################################################################
#                                                                                                         #
#   carray2bin.py                                                                                         #
#                                                                                                         #
#   Reverses the output of xxd -i converting a c file containing a single array of hex values back to bin #
#                                                                                                         #
#   Written by Peter Ing                                                                                  #
#   April 2022                                                                                            #
#                                                                                                         #
###########################################################################################################

from doctest import DocTestFailure
import re
import struct
import getopt
import sys



def convert2bin(sourcefile,destfile):
    buf =''
    hex=[]
    f = open(sourcefile).read() 
    buf = ''.join(f.split())
    buf = buf[buf.find('{')+1: buf.find('}')]
    pat = re.compile('0x[0-9a-fA-F]{2}')
    for h in re.findall(pat, buf):
        hex.append(h)
    try:
        with open(destfile, 'wb') as f:
            for binval in hex:
                f.write(struct.pack('B', int(binval, 16)))
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    infile =''
    outfile =''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"i:o:", ["inputfile=", "outputfile="])
    except getopt.GetoptError:
        print("Error check parameters")
        sys.exit(2)

    for optn ,argu in opts:
        if optn in ("-i", "--inputfile"):
            infile = argu
        elif optn in ("-o" , "--outputfile"):
            outfile = argu
    if infile =='' or outfile=='':
        print("Error check parameters")
        sys.exit(2)
    else:
        convert2bin(infile, outfile)
        print("Completed")
        
