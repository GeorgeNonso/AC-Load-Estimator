# Write your AC Load Estimator solution here
width = float(input("enter the room's width"))
height = float(input("enter the rooms hieght"))
number_of_people = int(input("enter the size of the people"))

horsepower = width * height * 0.1 + number_of_people * 0.06
print (horsepower)
