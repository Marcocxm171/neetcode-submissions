class MedianFinder:

    def __init__(self):
        self.array = []
        

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array = sorted(self.array)
        

    def findMedian(self) -> float:
        if len(self.array) % 2 == 0 : 
            idx_2 =  len(self.array)//2 
            median = (self.array[idx_2 -1] + self.array[idx_2])/2
        else: 
            idx = len(self.array)//2
            median = self.array[idx]

        return median
        
        