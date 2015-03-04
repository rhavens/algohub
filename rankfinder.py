###############################################################
# rankfinder.py
#
# A selection algorithm to determine the rank of an element $k in a 
# sorted array $A of $n distinct elements. Inspired by a question on
# an algorithms exam.
#
# The algorithm works by guessing the location of $k based on its
# relative position given the range and length of the array. It then
# uses this guess to partition and make further recursive guesses.
#
# Ryan Havens 3/4/2015
#
###############################################################

import random # need this to generate the array, otherwise junk

#################################################
# Base parameters for generating the array
# @max_range: The range of elements in the array, from 1 to max_range
# @max_size: The max size of the array, prior to removing duplicates
# @to_find: The element whose rank we're looking for
# @intarray: The array

max_range = 100
max_size = 100
to_find = 64

intarray = []

#################################################
# remove_duplicates(arr)
# @arr: An input array
# Returns the array with duplicates removed, free the original array after
#	unless you still need it.
# NOT stable
# WILL SORT
# Requires O(n) space
# Requires O(n^2logn) time

def remove_duplicates(arr):
	arr.sort()
	arr2 = []
	for i in xrange(1, len(arr)):
		if (len(arr2) == 0):
			arr2 = arr2 + [arr[i]]
		elif (arr[i] != arr2[len(arr2)-1]):
			arr2 = arr2 + [arr[i]]
	return arr2

#################################################
# get_rank(A, x, r)
# @A: The input array. Must be sorted.
# @x: The element we are searching for in the array
# @r: Helper variable to store index as we recurse. Should always be zero.
#	Could potentially be in a helper function instead.
# Returns the rank at which the element is found in the array, unless the
#	element does not exist, in which case it returns (-1)
# This *should* run, in the average case, in faster than O(logn) time..
# The recursion stack will take up a lot of space. Could theoretically be
#	improved by freeing the temporary array prior to each recursion call, or,
#	by storing local start and end indices instead of reconstructing the array
#	each time.

def get_rank(A, x, r):
	iMin = 0
	iMax = len(A) - 1
	if (iMax <= 0):
		return (-1)
	iRange = A[iMax] - A[iMin]
	iRel = int(round(((x - A[iMin])/(iRange*1.0))*(len(A)-1)))
	# try:
	# 	print "iRel {} A[iRel] {}".format(iRel, A[iRel])
	# except (IndexError):
	# 	print "iRel {} A[iRel] {}".format(iRel, "not in range")
	# print "r {}".format(r)
	if ((iRel > iMax) or (iRel < 0)):
		return (-1)
	if (x == A[iRel]):
		return r + iRel
	elif (x > A[iRel]):
		# print A[(iRel+1):]
		return get_rank(A[(iRel+1):], x, r + iRel + 1)
	else:
		# print A[:iRel]
		return get_rank(A[:iRel], x, r)

#################################################
# Junk code to generate a sorted array of distinct integers
# Works with remove_duplicates from above

intarray = []
for i in xrange(0, max_size):
	intarray = intarray + [random.randint(1,max_range)]
intarray = remove_duplicates(intarray)

#################################################
# Junk code for output

print(intarray)
print("length of intarray {}".format(len(intarray)))
n = get_rank(intarray, to_find, 0)
print("computed rank {}".format(n))
if (n >= 0):
	print("computed element {}".format(intarray[n]))
else:
	print("computed not found")