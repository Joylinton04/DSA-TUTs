def create_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix
    

def query_range(prefix, L,R):
    return prefix[R+1] - prefix[L]


arr = [3, 1, 4, 1, 5, 9, 2]
print(create_prefix_sum(arr))
print(query_range(create_prefix_sum(arr),1,3))