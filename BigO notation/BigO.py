#Logarithmic O(LogN) runtime
arr = [1,2,3,4,5,6]
# for i in range(0,len(arr), 3):
#     print(arr[i])

#logarithmic O(LogN) runtime
def binary_search(arr, num):
    if len(arr) == 0:
        return 'none'
    mid = len(arr) // 2
    if arr[mid] == num:
        return "found"
    elif arr[mid] > num:
        return binary_search(arr[:mid], num)
    else:
        return binary_search(arr[mid+1:], num)
    
# print(binary_search(arr, 10))