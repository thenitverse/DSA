# bubble sort
arr = list(map(int,input("enter numbers seperated by space : ").split()))
n = len(arr)
swapping = True
while swapping == True:
    swapping = False
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp
            swapping = True
    n -=1
print(arr)