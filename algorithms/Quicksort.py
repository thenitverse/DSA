nums = list(map(int , input("Enter numbers : ").split()))
def quick_sort(nums):
    if len(nums) <=1:
        return nums
    

    pivot = nums[-1]
    left = []
    right = []
    for i in nums[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    total = quick_sort(left)+[pivot]+quick_sort(right)

    return total

print("Your sorted llist: ",quick_sort(nums))