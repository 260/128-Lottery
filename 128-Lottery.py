#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/130

first_line  = input()
second_line = input()

budget              = int(first_line)
number_of_people    = int(second_line)

print(int(budget/1000/number_of_people)*1000)
