# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NdIFumn7WprEPC7_NtoA1PpHTOk2Y6Br
"""

#in this programe we take an input from the user and Slice that number upto
#two index and then we do typecasting from string to intger and then add that
#two number and save it into another variable and then we print the final result
num1 = input("Enter the number you want to slice:  ")
print("The number you entered is : ",num1)

num1_slice1 = num1[0]
print(num1_slice1)

num2_slice2 = num1[1]
print(num2_slice2)

add_num1 = int (num1_slice1)
add_num2 = int (num2_slice2)

add_two_number = add_num1 + add_num2

print("The Addition of two number is : ", add_two_number)

