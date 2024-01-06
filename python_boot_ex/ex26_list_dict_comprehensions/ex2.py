# 챌린지 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers]

print(squared_numbers)

# 챌린지 2
list_of_strings = input().split(",")
result = [result for result in list_of_strings if int(result) % 2 == 0]
print(result)

# 챌린지 3
with open("file1.txt", "r") as file1:
    file1_arr = file1.readlines()
with open("file2.txt", "r") as file2:
    file2_arr = file2.readlines()

result_arr = [int(item) for item in file1_arr if item in file2_arr]
print(result_arr)
