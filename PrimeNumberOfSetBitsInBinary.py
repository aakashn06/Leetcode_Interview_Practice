class Solution(object):
    def countPrimeSetBits(self, left, right):
        # Write prime checker function
        def isPrime(num):
            if num == 1:
                return False
            i = num // 2 
            possibleFactor = 2
            while possibleFactor <= i:
                if num % possibleFactor == 0:
                    return False
                possibleFactor += 1
            return True

        # Write set bit counter
        def set_bit_count(num):
            i = 7
            count = 0
            while i > -1:
                quotient = num / (2 ** i)
                if quotient >= 1:
                    count += 1
                num = num % (2 ** i)
                i -= 1
            return count
        
        count = 0
        i = left
        while i <= right:
            if isPrime(set_bit_count(i)):
                print(i)
                count += 1
            i += 1
        return count
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
