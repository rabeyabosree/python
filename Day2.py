students = []

while True:
    print("\n1 add student \2 show sudents \n3 search by roll \n4 delete students \n5 unique subject \n6 exist")

    # user choise 
    choise = input("enter your choise : ")

    # logical statment with if else
    # add student
    if choise == "1":
        name = input("name")
        age = int(input("age:"))
        roll = int(input("roll : "))
        subjects = tuple(input("subjects (comma separeted : )").split(","))

        student = {"name": name, "age": age, "roll": roll, "subjects": subjects}
        students.append(student)
        print("student added", student)

    elif choise == "2":
        for student in students:
            print(student)




    break