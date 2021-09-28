
I = lambda : map(int, input().split())


T = int(input())

for _ in range(T):
    n,k = I()
    a = list(I())
    a.sort()
    b = list(I())
    b.sort()
    
    l,r = 0,n-1
    for _ in range(k):
        if a[l] < b[r]:
            a[l] = b[r]
        l, r = l+1,r-1

    print(sum(a))
    
'''

'''
