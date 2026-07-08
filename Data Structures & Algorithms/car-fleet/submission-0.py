class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            time_to_finish = math.ceil((target - position[i]) / speed[i])
            stack.append((position[i], time_to_finish))
        
        stack = sorted(stack, key = lambda pos: pos[0])
        fleets = 0

        while stack:
            if len(stack) == 1:
                fleets += 1
                break
            if stack[-1][1] < stack[-2][1]:
                fleets += 1
                stack.pop()
            else:
                fleet_speed = stack[-1][1]
                stack.pop()
                stack.pop()
                stack.append((0, fleet_speed))
        
        return fleets
        