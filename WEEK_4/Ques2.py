class Ques2:
    def __init__(self, message):
        self.message = message
    def isPalindrome(self):
        self.message = self.message.lower()
        left = 0
        right = len(self.message) - 1
        while left < right:
            if self.message[left] != self.message[right]:
                return False
            left += 1
            right -= 1
        return True