class Solution:
    def RomanToInt(self, x:str):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        
        for char in reversed(x):
            current_value = roman_values[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
            
        return result
    
solution = Solution()
print(solution.RomanToInt("IX"))
