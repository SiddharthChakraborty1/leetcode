
# brute force O(n^2)
class Solution:

    def dailyTemperatures(self, temperatures):
        if not temperatures:
            return

        if len(temperatures) == 1:
            return [0]

        results = [0 for i in range(len(temperatures))]
        i, j = 0, 0
        temperature_len = len(temperatures)
        while i < temperature_len:
            current = temperatures[i]
            j = i+1
            distance = 1
            while j < temperature_len:
                if temperatures[j] > current:
                    results[i] = distance
                    break
                else:
                    distance += 1
                j +=1

            i += 1

        return results



# Optimized O(n)
class Solution:
    
    def dailyTemperatures(self, temperatures):
        
        stack = []
        results = [0 for i in range(len(temperatures))]
        
        i = 0
        while i < len(temperatures):
            if not stack:
                stack.append((i, temperatures[i]))
            else:
                while stack and stack[-1][1] < temperatures[i]:
                    popped_index, _ = stack.pop()
                    results[popped_index] = i - popped_index

                stack.append((i, temperatures[i]))
            
            i += 1
        
        return results


s = Solution()
inputs = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
print(s.dailyTemperatures(inputs))
