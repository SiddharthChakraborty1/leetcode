class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        min = None
        min =  self.recursive_search(left, right, piles, h, max(piles))
        return min
    
    def recursive_search(self, left, right, piles, h, result):
        if left > right:
            return result 
    
        mid = (left + right)//2
        iterations = self.get_iterations(piles, mid)
        if iterations <= h:
            result = mid
            return self.recursive_search(left, mid-1, piles, h, mid)
        elif iterations > h:
            return self.recursive_search(mid + 1, right, piles, h, result)
        
            
    def get_iterations(self, piles, k):
        iterations = 0
        for element in piles:
            hours  = element//k
            if element % k != 0:
                hours +=1 
            
            iterations += hours
        return iterations

s = Solution()
print(s.minEatingSpeed([4, 10, 23, 25], 4))
