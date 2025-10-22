#!/usr/bin/env python3

def get_input():
    user_input = input("User input: ")
    m = int(user_input) 
    if user_input.isdigit() and m > 0:
      return int(user_input)
    else:
      print("Error, enter valid input")

def get_calculation(m):
  a = 0
  b = 1
  sequence = []
  for i in range(m):
      sequence += [a]
      a, b = b, a + b
  return sequence


def fib_output(sequence):
  for num in sequence:
    print(num, end = " ")
  print(" ")

def main():
  m = get_input()
  sequence = get_calculation(m)
  fib_output(sequence)


main()
  
  
    

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
