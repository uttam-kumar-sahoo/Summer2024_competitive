class Solution:
    def armstrongNumber(self, n):
        original = n
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 3
            n //= 10
        return "Yes" if sum == original else "No"