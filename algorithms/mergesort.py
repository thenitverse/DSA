# merge sort
nums = list(map(int , input("enter numbers: ").split()))
def mrge_sort(nums):

    n = len(nums)
    if n <=1:
        return nums
    mid = len(nums)//2
    left = mrge_sort(nums[: mid])
    right = mrge_sort(nums[mid :])
    return merge(left,right)

def merge(left,right):
    final = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            final.append(left[i])
            i+=1
        else:
            final.append(right[j])
            j+=1

    while i < len(left):
        final.append(left[i])
        i+=1

    while j < len(right):
        final.append(right[j])
        j+=1

    return final


print("sorted list:",mrge_sort(nums))
    
    
    