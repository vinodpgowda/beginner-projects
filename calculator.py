# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program untill the user wants to exit

class Calculator:
    def __init__(self):
        print("Enter two values:")
        self.a = int(input("first number: "))
        self.b = int(input("second number: "))

    def add(self):
        result = self.a + self.b
        print(f'\n{self.a} + {self.b} is {result}')

    def sub(self):
        result = self.a - self.b
        print(f'\n{self.a} - {self.b} is {result}')

    def mul(self):
        result = self.a * self.b
        print(f'\n{self.a} * {self.b} is {result}')

    def div(self):
        result = self.a / self.b
        print(f'\n{self.a} / {self.b} is {result}')

def main():

    i = 1
    while(i):
        print("\nChoose any one opeartion:")
        operation = input("'a' for Addition, 's' for Subtraction, 'm' for Multiplication, 'd' for Division OR 'q' to exit: ")
        if operation == 'q':
            print("Bye")
            break
        if operation not in ('a', 's', 'm', 'd'):
            print("please enter a valid operation!\nOR enter 'q' to exit")
        else:
            if operation == 'a':
                print("You have selected addition operation")
                calculator = Calculator()
                calculator.add()
            elif operation == 's':
                print("You have selected subtraction operation")
                calculator = Calculator()
                calculator.sub()
            elif operation == 'm':
                print("You have selected multiplication operation")
                calculator = Calculator()
                calculator.mul()    
            else:
                print("You have selected multiplication operation")
                calculator = Calculator()
                calculator.div()


if __name__ == '__main__':
    main()