students = ["Benatic", "Rithan", "Arun", "Kavin", "Rahul"]

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

print("Student Search System")
print("1. Linear Search")
print("2. Binary Search")

choice = input("Enter Choice: ")
name = input("Enter Student Name: ")

if choice == "1":
    result = linear_search(students, name)

elif choice == "2":
    students.sort()
    result = binary_search(students, name)

else:
    print("Invalid Choice")
    exit()

if result != -1:
    print("Student Found at Index:", result)
else:
    print("Student Not Found")