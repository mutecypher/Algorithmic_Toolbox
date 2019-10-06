#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 09:44:12 2019

@author: mutecypher
"""
numbers = [ 3, 5, 7, 13, 5]
max_product = 0
maxnumb = max(numbers)
numbers.remove(max(numbers))
sec_max = max(numbers)
max_product = maxnumb * sec_max
print(max_product)

