#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:57:20 2019

@author: mutecypher
"""

# Uses python3
import sys
def recMC(coinValueList, change):
	minCoins = change
	if change in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c <= change]:
			numCoins = 1 + recMC(coinValueList, change-i)
			if numCoins < minCoins:
				minCoins = numCoins
	return minCoins

m = float(input())
print(recMC([1,5,10,25],63))