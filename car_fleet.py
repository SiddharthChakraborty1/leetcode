class Solution:
    def carFleet(self, target, positions, speed):
        
        # first we will sort the positions in descending order
        position_speed_mapper = {}
        for p, s in zip(positions, speed):
            position_speed_mapper[p] = s
        
        position_speed_mapper = dict(sorted(position_speed_mapper.items(), reverse=True))
        position_time_mapper = {
            p: (target - p)/s for p,s in position_speed_mapper.items()
        }
        print(position_time_mapper)
        
        stack = []
        for position, time in position_time_mapper.items():
            if not stack:
                stack.append(time)
            else:
                st = stack[-1]
                if time <= st:
                    continue
                else:
                    stack.append(time)
        
        return len(stack)
        
        
