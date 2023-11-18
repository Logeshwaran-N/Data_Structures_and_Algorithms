a=[5,6,7,8,1,2,3,4]
b=[5,6,7,8,9,10,11,1,2,3,4]
c=[8,9,1,2,3,4,5,6,7]
d=[1,2,3,4]
e=[1]
expected=4

def binary_serch(a):

    start=0
    end=len(a)-1
    mid = (start+end) // 2
    if len(a) <= 1 or a[start] < a[end]:
        return  0
    while True:
        mid = (start + end) // 2
        tmid, tsta, tend = a[mid], a[start], a[end]
        if mid == start and end == mid+1:
            return mid+1
        if a[mid] > a[start]:
            start=mid
        else:
            end=mid


print(binary_serch(a))
print(binary_serch(b))
print(binary_serch(c))
print(binary_serch(d))
print(binary_serch(e))
