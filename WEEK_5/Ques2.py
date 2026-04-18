class Ques2:
    def __init__(self):
        self.arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.arr2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    def operations(self):
        
        # Addition
        addition = [[self.arr1[i][j] + self.arr2[i][j] for j in range(len(self.arr1[0]))] for i in range(len(self.arr1))]
        print("\nAddition of Array 1 and Array 2:")
        for row in addition:
            print(row)
        
        # Subtraction
        subtraction = [[self.arr1[i][j] - self.arr2[i][j] for j in range(len(self.arr1[0]))] for i in range(len(self.arr1))]
        print("\nSubtraction of Array 1 and Array 2:")
        for row in subtraction:
            print(row)
        
        # Multiplication
        multiplication = [[self.arr1[i][j] * self.arr2[i][j] for j in range(len(self.arr1[0]))] for i in range(len(self.arr1))]
        print("\nMultiplication of Array 1 and Array 2:")
        for row in multiplication:
            print(row)
        # Division
        division = [[self.arr1[i][j] / self.arr2[i][j] for j in range(len(self.arr1[0]))] for i in range(len(self.arr1))]
        print("\nDivision of Array 1 and Array 2:")
        for row in division:
            print(row)
        # Modulus
        modulus = [[self.arr1[i][j] % self.arr2[i][j] for j in range(len(self.arr1[0]))] for i in range(len(self.arr1))]
        print("\nModulus of Array 1 and Array 2:")
        for row in modulus:
            print(row)