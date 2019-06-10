def triplet(a):
    a.sort()
    print (a)
    for i in range(len(a)-2):
        if ((a[i] < (a[i+1] + a[i+2])) and
            (a[i+2] < (a[i] + a[i+1])) and
                (a[i+1] < (a[i] + a[i+2]))):
            print (a[i], " ", a[i+1], " ",a[i+2])
            return 1
    return 0



if __name__ == '__main__':
    arr = [1,2,4,6,32,45,43,54,65,76,78,32,56]
    triplet(arr)
