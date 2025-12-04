#A set of data within square brackets

fruits = ["betik" , "durian" , "rambutan" , "langsat"]
numbers = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10,]
mixed = ["abc", 456, False, True, 33.3]

print(fruits[0])
print (numbers[0])
print (mixed[0])

print(fruits[-1])
print(numbers[-1])
print(mixed[-1])

print(fruits[1:4])
print(numbers[1:4])
print(mixed[1:4])

print(fruits[:3])
print(numbers[:3])
print(mixed[:3])

print(fruits[2:])
print(numbers[2:])
print(mixed[2:])


#SETS

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10,}
set3 = {3, 4, 5}

print (set1.union(set2))
print(set1.intersection(set3))  #data yang sama
print(set1.difference(set2))

#EXERCISE

#Create a system that stores student grades as tuples (name, subject, grade ) and uses sets to find unique subjects and students
#grades=[
#("Alice, "Math" , 85) ("Bob" , " Science , 92) ("Alice" , "Science" , 78) ("Charlie" , "Math" , 90) ("Bob" , "Math" 88) ("Alice" "English" 95)

# List of tuples (name, subject, grade)
grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88)
]

unique_students = {entry[0] for entry in grades}
unique_subjects = {entry[1] for entry in grades}

print("Unique Students:", unique_students)
print("Unique Subjects:", unique_subjects)

