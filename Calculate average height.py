# Program to calculate average height from a list of heights

heights_input = input("Enter all heights separated by a space: ")
heights_list = heights_input.split()
heights = [int(height) for height in heights_list]
number_of_heights = len(heights)
total_height = sum(heights)
average_height = total_height / number_of_heights
print("Average height is:", round(average_height))
