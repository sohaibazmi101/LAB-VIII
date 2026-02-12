class Ques3:
    def __init__(self):
        self.students ={
            "Ayaan Khan": 82,
            "Zara Ahmed": 91,
            "Mohammed Arif": 68,
            "Fatima Sheikh": 77,
            "Imran Ali": 72,
            "Sana Parveen": 88,
            "Rehan Siddiqui": 74
        }
    def highest_score(self):
        for name, marks in self.students.items():
            if marks > 75:
                print(name, ":", marks)