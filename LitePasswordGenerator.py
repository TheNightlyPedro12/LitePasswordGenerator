#!/usr/bin/python3
import random as r
sc = "[]{}#%^*+=-/:;()$&@.,?!"
def sqgen():
	p = chr(r.randint(ord('A'), ord('Z')))
	p = p + chr(r.randint(ord('a'), ord('z')))
	p = p + str(r.randint(0,9))
	p = p + r.choice(sc)
	return(p)
print("Your generated password is: " + sqgen() + sqgen() + sqgen() + sqgen())
