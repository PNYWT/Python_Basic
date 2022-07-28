# create and use function
from email import message
from unicodedata import name


def funcName():
    print("Now Use funcName")

funcName()

# Global Variable / Local Variable
def displayNumber():
    x = 10
    print("x is =",x)

displayNumber()

#Pass data to func
def myName(name):
    print("My name is", name)
myName("Pun.")

#Return Func
def returnFunc(num1,num2):
    total = num1+num2
    return total
print(returnFunc(10,20))

#func call func
def func1():
    print('func1')

def func2():
    func1()
    print('func2')
func2()


#Assignement
data = {"1122":"Pizza",
    "1150":"KFC"
}
#คำตอบแบบที่ 1
def searchNumber(number):
    for i,j in data.items():
        if i == number:
            print("Number is", i ,"Call to",j)
        else:
            print("No Data")

searchNumber("1122")

#คำตอบแบบที่ 2
def searchNumber2(number):
    print("Number is", number, "Call to", data[number])

searchNumber2("1150")