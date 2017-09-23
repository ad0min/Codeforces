
def main():
#	n = input()
	n = "123987"
	pre = n[0:3]
	post = n[3:6]
	pre_sum = Sum(int(pre))
	post_sum = Sum(int(post))
	mi =[]
	if (pre_sum == post_sum):
		return 0
	if(pre_sum > post_sum):
		diff = pre_sum - post_sum
		mi = list(map(int,post))
		ma = list(map(int,pre))
	else:
		diff = post_sum - pre_sum
		mi = list(map(int,pre))
		ma = list(map(int,post))
	count = 0
	while diff :
		inc = 9 - min(mi)
		dec	= max(ma)- 0
		print(dec)
		if diff > inc and inc >= dec:
			count +=1
			mi[mi.index(min(mi))] = 9
			diff -= inc
			print("mi",mi)
			print("ma",ma)
			print("diff",diff)
			print("++++++++++++++in")
		if diff > dec and  inc < dec:
			count +=1
			ma[ma.index(max(ma))] = 0
			diff -= dec

			print("mi",mi)
			print("ma",ma)
			print("diff",diff)
			print("++++++++++++++dc")
		if diff <= (max(ma)- 0) or diff <= (9 - min(mi)):
			diff =0
		print("mi",mi)
		print("ma",ma)
		print("diff",diff)
		print("++++++++++++++")
	return count+1


def Sum(n):
	s =0
	while n:
		s += n%10
		n = n//10
	return s

print(main())