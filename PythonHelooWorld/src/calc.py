'''
Created on Feb 17, 2018

@author: Karandeep.Singh
'''
def add(num1, num2):
    return num1 + num2

def multiple(num1, num2):
    return num1 * num2
    
def division(num1, num2):
    return num1/num2
            
def subtract(num1, num2):
    return num1 - num2
    
def main():
    EnterOperation = input("please select one operation(+,*,/,-) : " )
    if(EnterOperation == '+' and EnterOperation == '-' and EnterOperation == '/' and EnterOperation == '*'):
        print("enter a valid operation")
    else:
        var1 = int(input("Enter num1: "))
        var2 = int(input("Enter num2: "))
        if(EnterOperation == '+'):
            print(add(var1, var2))
        elif(EnterOperation == '-'):
            print(subtract(var1, var2))
        elif(EnterOperation == '*'):
            print(multiple(var1, var2))
        else:
            print(division(var1, var2))
        
        
main()