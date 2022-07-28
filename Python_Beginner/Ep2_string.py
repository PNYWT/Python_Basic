name = "4444 5555 6666"
print(name.replace("5555","2"))

numberInName = "5" in name

if numberInName:
    name = name.replace("5","B")
print(name)


#MARK: Format
fname = "Pun"
lname = "Suw"
age = "25"
fullName = "MR.: {0} {1}, age: {2}"
theFull = fullName.format(fname,lname,age).lower()
# print(theFull)

if theFull.startswith("MR.:".lower()):
    print("Result",theFull.replace("MR.:".lower(),"นาย"))
else:
    print("False")