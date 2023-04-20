#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:49:34 2022

@author: Oshen Wijesundara
"""

#assign variables (candidates)
x=0
a=0
b=0
c=0
d=0
e=0
r=0

while x<51:
    #if x==51:#
        #break#
    q= input("Candidate you would vote to: ").lower()#input function always takes a string#
    if q == "a":
        a += 1
        
    elif q == "b": 
        b += 1
        
    
    elif q == "c": 
        c += 1
        
        
    elif q == "d": 
        d += 1
        
    elif q == "e": 
        e += 1
       
    else: 
        
        print('Vote rejected')
        r+=1
        
    x+=1
        

print('No.of votes for A:', a)
print('')
print('No.of votes for B:', b)
print('')

print('No.of votes for C:', c)
print('')

print('No.of votes for D:', d)
print('')

print('No.of votes for E:', e)
print('')
print('')
print('')
print('')
print('')


arr= [a, b, c, d, e]#array is not in phython# 

arr.sort()#array is now in ascending order#

p=arr[-1]
s=arr[-2]
vs=arr[-3]
vp=arr[-4]
t=arr[-5]

for i in [a,b,c,d,e]:
    if i == a:
        print('President is A')
    elif i ==b:
        print('President is B')
    
if b == p:
    print("President is B")
    print('')

    
if c == p:
    print("President is C")
    print('')

if d == p:
    print("President is D")
    print('')

if e == p:
    print("President is E")
    print('')




if a == s:
    print("Secretary is A")
    print('')

if b == s:
    print("Secretary is B")
    print('')

    
if c == s:
    print("Secretary is C")
    print('')

if d == s:
    print("Secretary is D")
    print('')

if e == s:
    print("Secretary is E")
    print('')

    
    

if a == vs:
    print("Vice Secretary is A")
    print('')

if b == vs:
    print("Vice Secretary is B")
    print('')

    
if c == vs:
    print("Vice Secretary is C")
    print('')

if d == vs:
    print("Vice Secretary is D")
    print('')

if e == vs:
    print("Vice Secretary is E")
    print('')

    


if a == vp:
    print("Vice President is A")
    print('')

if b == vp:
    print("Vice President is B")
    print('')

    
if c == vp:
    print("Vice President is C")
    print('')

if d == vp:
    print("Vice President is D")
    print('')

if e == vp:
    print("Vice President is E")
    print('')

    

if a == t:
    print("Treasurer is A")
    print('')

if b == t:
    print("Treasurer is B")
    print('')

    
if c == t:
    print("Treasurer is C")
    print('')

if d == t:
    print("Treasurer is D")
    print('')

if e == t:
    print("Treasurer is E")
    print('')

    

    
    

    
    





