try:
    number1 = int(input("Number 1 :"))
    number2 = int(input("Number 2 :"))
    if number1<0 or number2<0:
        raise Exception("ป้อนค่าติดลบไม่ได้")
    result = number1/number2
    print(result)
except Exception as e:
    print("Error :", e)

# I think this func like try{} catch{} in swift