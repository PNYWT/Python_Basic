#BMI
# BMI = weight (kg) / height^2 (m)

weight = float(input("Input your wegiht : "))
height = float(input("Input your height : "))/100
BMI = weight /(height**2)

if BMI < 18.50:
    print("BMI : {:.2f} น้ำหนักน้อย / ผอม".format(BMI))
elif BMI >= 18.50 and BMI <= 22.90:
    print("BMI : {:.2f} เท่าคนปกติ".format(BMI))
elif BMI >= 23.00 and BMI <= 24.90:
    print("BMI : {:.2f} ท้วม / โรคอ้วนระดับ 1".format(BMI))
elif BMI >= 25.00 and BMI <= 29.90:
    print("BMI : {:.2f} ท้วม / โรคอ้วนระดับ 2".format(BMI))
else:
    print("BMI : {:.2f} ท้วม / โรคอ้วนระดับ 3".format(BMI))
