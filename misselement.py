def missing_element(a):
    a.sort()
    for i in range (len(a)):
        if i+1 != a[i]:
            return (i+1)


if __name__ == '__main__':
    arr = [1,2,4,5]
    ME=missing_element(arr)
    print(ME)
