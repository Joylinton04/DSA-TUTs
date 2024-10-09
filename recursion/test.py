def capitalizeWords(arr):
    result = []
    if len(arr) == 0: return arr
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

array = ['i', 'am', 'a', 'boy']
print(capitalizeWords(array))  