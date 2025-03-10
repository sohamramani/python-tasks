# CALCULATION CLASS 
class Calculate:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def Addition(self, num1, num2):
        return num1 + num2
    
    def Subtraction(self, num1, num2):
        return num1 - num2
    
    def Multiplication(self, num1, num2):
        return num1 * num2
    
    def Division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    def Power(self, num1,num2):
        return num1 ** num2
    
    def Remainder(self, num1, num2):
        return num1 % num2
    
    def Bitwise_Left_Shift(self, num1, num2):
        return num1<<num2
    
    def Bitwise_Right_Shift(self, num1, num2):
        return num1>>num2
    
    def Bitwise_AND(self, num1, num2):
        return num1 & num2
    
    def Bitwise_OR(self, num1, num2):
        return num1 | num2
    
    def Bitwise_XOR(self, num1, num2):
        return num1 ^ num2
    
    def Bitwise_NOT(self, num1, num2):
        return ~num1 , ~num2
    
    def Less_Than(self, num1, num2):
        return num1 < num2
    
    def Greater_Than(self, num1, num2):
        return num1 > num2
    
    def Equal_To(self, num1, num2):
        return num1 == num2
    
    def Not_Equal_To(self, num1, num2):
        return num1 != num2
    
    def Less_Than_Or_Equal_To(self, num1, num2):
        return num1 <= num2
    
    def Greater_Than_Or_Equal_To(self, num1, num2):
        return num1 <= num2

# USER INPUT TWO NUMBERS
num1 = int(input("Enter first number : " ))
num2 = int(input("Enter secound number : "))

# CALCULATION OBJECT TO CALCULATE TWO NUMBERS
calculation = Calculate(num1,num2)

# ALL MATH CALCULATION OF TWO NUMBERS 
print("Addition of two number is : ",calculation.Addition(num1,num2))
print("Subtraction of two number is : ",calculation.Subtraction(num1,num2))
print("Multiplication of two number is : ",calculation.Multiplication(num1,num2))
print("Division of two number is : ",calculation.Division(num1,num2))
print("Power of two number is : ",calculation.Power(num1,num2))
print("Remainder of two number is : ",calculation.Remainder(num1,num2))
print("Bitwise Left Shift of two number is : ",calculation.Bitwise_Left_Shift(num1,num2))
print("Bitwise Right Shift of two number is : ",calculation.Bitwise_Right_Shift(num1,num2))
print("Bitwise AND of two number is : ",calculation.Bitwise_AND(num1,num2))
print("Bitwise OR of two number is : ",calculation.Bitwise_OR(num1,num2))
print("Bitwise XOR of two number is : ",calculation.Bitwise_XOR(num1,num2))
print("Bitwise NOT of two number is : ",calculation.Bitwise_NOT(num1,num2))
print("Less than is : ",calculation.Less_Than(num1,num2))
print("Greater than is : ",calculation.Greater_Than(num1,num2))
print("Equal to is : ",calculation.Equal_To(num1,num2))
print("Not Equal to is : ",calculation.Not_Equal_To(num1,num2))
print("Less than or equal to is : ",calculation.Less_Than_Or_Equal_To(num1,num2))
print("Greater than or equal to is : ",calculation.Greater_Than_Or_Equal_To(num1,num2))
