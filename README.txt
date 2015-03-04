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

The meat:

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
#	improved by freeing the temporary array prior to each recursion call, 
#	or, by storing local start and end indices instead of reconstructing 
#	the array each time.