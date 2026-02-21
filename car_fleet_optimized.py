class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        pairs = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        for pos, spd in pairs:
            time_taken = (target-pos)/spd
            if not stk or time_taken > stk[-1]:
                stk.append(time_taken)
        
        return len(stk)
