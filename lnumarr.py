def largest(arr,n):
	max = arr[0]
	for i in range(1,n):
		if arr[i] > max:
			max = arr[i]
	return max

arr = [10,13,5,50,90]
n = len(arr)
Ans = largest(arr,n)
print ("largest in the array",Ans)
