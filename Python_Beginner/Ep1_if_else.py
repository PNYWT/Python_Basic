from tkinter import S


age = int(input("Input Age : "))

if age >= 15 and age < 20: # if
    print("Age ", age, "Hi Teen")
    if age >= 18 and age < 20:
        print("Age ", age, "He can buy Beer")
elif age >= 20 and age > 15: # else if 
    print("Age ", age, "Hi Mr.")
else :                      # else
    print("Age ", age, "Hello Kid")