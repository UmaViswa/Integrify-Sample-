def recc(y):
	if y < 8:
		print("Current value of y:%s" %y)
		return recc(y = y + 1)
	print ("Course Passed")
if __name__ == "__main__":
	n = int(input("Enter a number:"))
	if ((n >= 0) and (n <= 10)): 
		if n < 5:
			recc(n)
		else: 
			n = n + 1
			print("Current Value of n:%s" %n)
	else:
		print("Enter a valid value between 0 and 10")


