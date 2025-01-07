numbers = input("Entetr list of numnbers>> ")
numbers_list = numbers.split()
count = 0

for number in numbers_list:
    count = count + 1
print(f"The length of the list is {count}")

for i in range(count):
    numbers_list[i] = int(numbers_list[i])
maximun_number = numbers_list[0]

for number in numbers_list:
    if number > maximun_number:
        maximun_number = number
print(f"The maximum number is {maximun_number}")