#!/usr/bin/env python3

import sys


def main(numbers):
    total = 0
    for i in numbers:                    # for every number(i) in numbers(list) 
        num = int(i)                     # num == integer
        total += num                     # add to total
    average = total / len(numbers)       # calculate average of the numbers in this function
    return average                       # return the average 


def get_args():
    input_one = sys.argv[1:]
    return input_one


# main
if __name__ == '__main__':
    numbers = get_args()
    average = main(numbers)
    print(average)