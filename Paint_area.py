import math
def paint_calculation(height,width,covers):
    area = height*width
    numbers_of_cans = math.ceil(area/covers)
    print(f"You will need {numbers_of_cans} cans of paint.")
hit = int(input("Enter a height of wall in meter:\n"))
wid = int(input("Enter a width of wall in meter:\n"))
coverage = 7
paint_calculation(height = hit,width = wid, covers = coverage)
