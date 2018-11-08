def insertion_sort(a):
    b=[]
    b.append(a[0])
    for i in range(len(a)-1):
        key=a[i+1]
        for j in range(len(b)):
            if key<b[j]:
                b.insert(j,key)
                break
            elif key>b[len(b)-1]:
                b.append(key)
    return b
a=[5,2,4,6,1,3]
a=insertion_sort(a)
print(a)