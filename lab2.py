#комментарий.
firstname = "Ramil"
surname = "Yergazinov"

grade = int(input())
if grade == 1:
    print("политех лучше всех!")
elif grade <= 4: 
    print ("добро пожаловать", firstname, surname)

else:
    print("введено неверное значение")
    