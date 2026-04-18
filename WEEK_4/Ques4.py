class Ques4:
    def __init__(self):
        self.number = [7,3,6,9,6,3,2,1,12,41,21]
    def decreasing_order(self):
        return sorted(self.number, reverse=True)
    def increasing_order(self):
        return sorted(self.number)