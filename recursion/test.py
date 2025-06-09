def capitalizeWords(arr):
    result = []
    if len(arr) == 0: return arr
    result.append(str(arr[0][0]).upper() + str(arr[0][1:]))
    return result + capitalizeWords(arr[1:])

array = ['i', 'am', 'a', 'boy']
# print(capitalizeWords(array))  


    
    
courses = {
    "digital system": 86,
    "ceng": 90
}


