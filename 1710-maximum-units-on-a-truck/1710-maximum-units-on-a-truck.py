class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda k: k[1], reverse=True)
        # print(boxes)
        ans = 0 
        for box in boxes:
            num_box = min(box[0], truckSize)
            truckSize -= num_box
            ans += num_box * box[1]
        return ans
            
                      
        
        