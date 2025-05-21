apples = int(input("Enter the number of Apples: "))
childs = int(input("Enter the number of Students: "))

everyStudentGets = int(apples / childs)
print("Every student should get " + str(everyStudentGets))

remainedInBasket = apples % childs
print("Apples remained in the Basket: " + str(remainedInBasket))