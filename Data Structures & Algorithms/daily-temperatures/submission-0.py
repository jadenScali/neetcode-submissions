class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack:
                min_i, min_t = stack[-1]
                if min_t < temp:
                    stack.pop()
                    result[min_i] = i - min_i
                else:
                    break

            stack.append((i, temp))
        
        return result
            
            

                