def unique(a):
	new_a =[]
	#print (set(a))
	for i in a:
		e = abs(i)
		new_a.append(e)
	new_a=set(new_a)
	print(len(new_a))

def opt_unique(a):
	for i in range(len(a)):
		a[i]=abs(a[i])
	#print(set(a))
	#print(len(a))
	return (len(set(a)))



if __name__ == '__main__':
	arr=[-1,-2,0,1,2,3,4,5,4]
	#unique(arr)
	distinct_count = (opt_unique(arr))
	print (distinct_count)
