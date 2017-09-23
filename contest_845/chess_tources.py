from collections import Counter

def Chess_tourney():
	n = int(input())
	array = list(map(int,input().split()))
	Quicksort(array,0,2*n-1)
	if (array[n] == array[n-1]):
		return "NO"
	return "YES"

#	return "YES"

def Quicksort(array,p,r):
	if (p< r): 
		q = Partition(array,p,r)
		Quicksort(array,p,q-1)
		Quicksort(array,q+1,r)

def Partition(array,p,r):
	x = array[r]
	i = p-1
	for j in range(p,r) :
		if array[j]<x:
			i += 1
			Swap(array,i,j)
	Swap(array,i+1,r)
	return i+1

def Swap(array,i,j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp

print (Chess_tourney())