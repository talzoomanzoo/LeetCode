class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        n = len(s)
        
        for i in range(n):
            current_val = roman_int_list[s[i]]
            
            if i + 1 < n and current_val < roman_int_list[s[i + 1]]:
                sum -= current_val
            else:
                sum += current_val
                
        return sum