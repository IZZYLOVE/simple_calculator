# This is a sample Python script.
class calc:
    def add(self):
        self.n1=float(n1)
        self.n2=float(n2)
        self.operator=operator
        result=(self.n1 + self.n2)
        print(f"{self.n1} {self.operator} {self.n2} = {result}")


    def rem(self):
        self.n1=float(n1)
        self.n2=float(n2)
        self.operator=operator
        result=(self.n1 - self.n2)
        print(f"{self.n1} {self.operator} {self.n2} = {result}")

    def mult(self):
        self.n1=float(n1)
        self.n2=float(n2)
        self.operator=operator
        result=(self.n1 * self.n2)
        print(f"{self.n1} {self.operator} {self.n2} = {result}")

    def div(self):
        self.n1=float(n1)
        self.n2=float(n2)
        self.operator=operator
        result=(self.n1 / self.n2)
        print(f"{self.n1} {self.operator} {self.n2} = {result}")

    def __init__(self, n1, operator, n2):
        self.n1=n1
        self.operator=operator
        self.n2=n2
        print("...PROCESSING...")
        if self.operator == '-':
            self.rem()

        elif self.operator  == '+':
            self.add()

        elif self.operator  == '/':
            self.div()

        elif self.operator  == '*' or self.operator  == 'x':
            self.mult()

        else:
            print('invalid operator!')
            print("...TERMINATED...")

print("SIMPLE CALCULATOR")
n1=float(input('Enter first number: '))
print ("accepted operators are (x or *) for multiplication, / for division, + for addition, - for subtraction")
operator=input('Enter operator: ')
n2=float(input('Enter second number: '))
calc(n1, operator, n2)
