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
    
    def IntToRoman(self, x):
        roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        
        for value, roman in roman_map:
            while x >= value:
                result += roman
                x -= value
        return result
    
    
    
solution = Solution()
print(solution.IntToRoman(0))