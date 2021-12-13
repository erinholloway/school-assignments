# function to compute BMI
def calculate_BMI(height, weight):
	bmi = weight * (703 / (height**2))
	return bmi




# function to determine category
def category_determine(bmi):
	if bmi < 18:
		return "underweight"
	elif 18 <= bmi <= 30:
		return "normal weight"
	else:
		return "overweight" 



# main
# initializing variables
bmi_list = []
underweight_count = 0
normalweight_count = 0
overweight_count = 0


# taking 6 names from user
name1, name2, name3, name4, name5, name6 = input("Enter 6 names (comma separated): ").split(",")
# making a list with given names
names = [name1, name2, name3, name4, name5, name6]


# using for loop taking height and weight for each name
for index in range(len(names)):
	print("\nEnter height of "+names[index]+" (inches): ",end="")
	height = float(input())
	print("Enter weight of "+names[index]+" (pounds): ",end="")
	weight = float(input())
	# calling the function
	bmi = calculate_BMI(height, weight)
	# appending  bmi to the bmi_list
	bmi_list.append(bmi)




print()


# using for loop to decide category
for bmi in bmi_list:
	# calling the function
	category = category_determine(bmi)
	
	# besed on the category incrementing the count of appropriate category
	if category == "underweight":
		underweight_count += 1
	elif category == "normal weight":
		normalweight_count += 1 
	else:
		overweight_count += 1
	# printing the person falls in which category
	print(names[bmi_list.index(bmi)]+" is in "+category)


print()


# printing count of each category
print("Underweight:",underweight_count)
print("Normal weight:",normalweight_count)
print("Overweight:",overweight_count)

input("press ENTER to exit.")

