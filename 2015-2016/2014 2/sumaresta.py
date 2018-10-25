import sys

d = int(input())

sumo = 14
sume = 16


res=(sumo*3+sume)%10

if res==0:
	res=10-res

print d ,res
