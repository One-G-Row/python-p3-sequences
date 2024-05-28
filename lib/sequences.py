#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]
    
    while len(sequence) < length:
        next = sequence[-1] + sequence[-2]
        sequence.append(next)
    print(sequence) 

print_fibonacci(9)
