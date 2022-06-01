class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the card according to position
        # if previous car reaching time is lower/equal than next car reaching time then previous car will reach faster or equal they will merge
        
        pair = [[p,s] for p,s in zip(position, speed)]
        pair = sorted(pair)
        
        stack = []
        """
        p = 0, 5
        v = 1, 1
        d = 12, 7
        t = 12, 7
        """
        
        """
        p = 6, 8
        v = 3, 2
        d = 4, 2
        t = 1.33, 1
        
        """
        
        for prev_car in reversed(pair):
            
            if stack:
                top = stack[-1]
                t_next = ((target-top[0])/top[1])
                t_prev = (target-prev_car[0])/prev_car[1]
                
                if t_prev <= t_next: # single fleet, merge
                    continue
            
            stack.append(prev_car)
        return len(stack)