import random

names = input("Enter everybody's name separated by comma: ")
names_list = names.split(",")
print(f"{random.choice(names_list)} will pay the bill")
