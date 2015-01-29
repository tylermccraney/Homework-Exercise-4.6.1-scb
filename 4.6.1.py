#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# 4.6.1 Exercises
# How many times will 'hello' be printed?
# 1)
for i in range(3, 17):
	print('hello')
	## 14 times
	
# 2)
for j in range(12):
	if j % 3 == 0:
		print('hello')
		## 4 times

# 3)
for j in range(15):
	if j % 5 == 3:
		print('hello')
	elif j % 4 == 3:
		print('hello')
		## 5 times

# 4)
z = 0
while z != 15:
	print('hello')
	z = z + 3
	## 5 times

# 5)
z = 12
while z < 100:
	if z == 31:
		for k in range(7):
			print('hello')
	elif z == 18:
		print('hello')
	z = z + 1
	## 8 times

# What does fooXX do?
def foo1(x):
	return x ** 0.5
	## takes square root of x
	
def foo2(x, y):
	if x > y:
		return x
	return y
	## finds the bigger number 
	
def foo3(x, y, z):
	if x > y:
		tmp = y
		y = x
		x = tmp
	if y > z:
		tmp = z
		z = y
		y = tmp
	if x > y:
		tmp = y
		y = x
		x = tmp
	return [x, y, z]
	## finds the biggest number and returns a list

def foo4(x):
	result = 1
	for i in range(1, x + 1):
		result = result + i
	return result
	## counts 1,2,3,4,5....

# This is a recursive function
# meaning that the function calls itself
# read about it at
# en.wikipedia.org/wiki/Recursion_(computer_science)
def foo5(x):
	if x == 1:
		return 1
	return x * foo5(x-1)
	## multiplies any number x (besides x=1) by 1 less than itself 