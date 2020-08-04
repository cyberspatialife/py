#!/usr/bin/env python3
import sys


def readfiles(file_name):
    with open(file_name, 'r') as f:
        #read_file = f.read #reads file 
        #read_file = f.read().split() #splits into a list
        read_file = f.read().strip() #strips empty lines
        
    return read_file
    
#def parse_file(file_name)
    #f = open(file_name, 'r')
    #read_file = f.read()
    #return read_file

def main():
    #takes in argument(file) index one
    input_one = sys.argv[1]
    #new variable calling on def readfiles
    print(readfiles(input_one))
    #prints out result variable
main()
