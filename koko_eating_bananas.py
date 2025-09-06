class Solution:
    def minEatingSpeed(self, piles, target_hours):
        slowest_speed = 1
        fastest_speed = max(piles)
        return self.recursive_search(slowest_speed, fastest_speed, piles, target_hours, fastest_speed)
    
    def recursive_search(self, slowest_speed, fastest_speed, piles, target_hours, result):
        if slowest_speed > fastest_speed:
            return result 
    
        speed_to_be_searched = (slowest_speed + fastest_speed)//2
        hours = self.get_hours_for_given_speed(piles, speed_to_be_searched)
        if hours <= target_hours:
            result = speed_to_be_searched
            return self.recursive_search(slowest_speed, speed_to_be_searched-1, piles, target_hours, speed_to_be_searched)
        elif hours > target_hours:
            return self.recursive_search(speed_to_be_searched + 1, fastest_speed, piles, target_hours, result)

    def get_hours_for_given_speed(self, piles, given_speed):
        hours = 0
        for element in piles:
            temp_hours  = element//given_speed
            if element % given_speed != 0:
                temp_hours +=1 
            
            hours += temp_hours
        return hours

s = Solution()
print(s.minEatingSpeed([4, 10, 23, 25], 4))
