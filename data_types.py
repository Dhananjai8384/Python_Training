# numbers = [10,20,30,40]

# numbers.append(50)

# numbers.remove(20)

# print("Updated List:", numbers)

# print("First Element:", numbers[0])

# print("All Numbers:")
# for num in numbers:
#     print(num)

my_tuple = (1, 2, 3, "hello", 4.5)
print("Tuple:", my_tuple)

print("First Element:", my_tuple[0])
print("All Elements:")
for num in my_tuple:
    print(num)

#unpacking a tuple
a,b,c,d,e = my_tuple
print("Unpacked Values:", a, b, c, d, e)


#sets are unordered collections of unique elements
my_set = {1, 2, 3, 3}
print("Set:", my_set)
my_set.add(4)
my_set.remove(2)
print("Updated Set:", my_set)


#dictionary
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}

print("Name:", employee["name"])

employee["department"] = "IT"

# Update
employee["salary"] = 60000

# Remove
employee.pop("id")

# Print dictionary
print("Updated Dictionary:", employee)

# Loop through dictionary
for key, value in employee.items():
    print(key, ":", value)