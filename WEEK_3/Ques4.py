class Ques4:
    def __init__(self, text):
        self.text = text
    def count_vowels(self):
        count = 0
        vowels = 'aeiouAEIOU'
        for char in self.text:
            if char in vowels:
                count += 1
        return f"The number of vowels in the <{self.text}> is: {count}"