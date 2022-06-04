class TimeMap:

    def __init__(self):
        self.data = {}
       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([value,timestamp])
        else:
            self.data[key] = [[value, timestamp]]
      
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.data:
            return ""
        sub_data = self.data[key]
        low = 0
        high = len(sub_data) - 1
        
        if sub_data[low][1] > timestamp:
            return ""
        
        while low <= high:
            m = low + (high-low)//2
            
            if sub_data[m][1] < timestamp:
                low = m+1
            elif sub_data[m][1] > timestamp:
                high = m-1
            else:
                # print(self.data[m][1])
                return sub_data[m][0]

                
        return sub_data[high][0]
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)