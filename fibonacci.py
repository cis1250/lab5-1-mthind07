#!/usr/bin/env python3

def get_input():
  user_input = input("User input: ")
  if user_input.isadigit() and int(user_input) > 0:
    return int(user_input)
  else:
    print("Error, enter valid input")

def get_calculation(i):
  a = 0
  b = 1
  for _ in range(i):
      a, b = b, a + b

def fib_output(sequence):
  for num in sequence:
    print(num, end = " ")
  print(" ")

def main():
  get_input()
  get_calculation(get_input))
  fib_output(get_calculation))


main()
  
  
    

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
