#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:24:34 2026

@author: raphaelivsic
"""

age = int(input("How old are you"))
if age >= 18 : 
    print("You can Vote")
elif age >15 :
    print(f"you will be able to vote in {18 - age} years")
else:
    print("You cna't vote")
        