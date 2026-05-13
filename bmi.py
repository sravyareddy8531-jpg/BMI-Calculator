print("===== BMI CALCULATOR =====")

# Taking input from user
weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in meters: "))

# BMI Formula
bmi = weight / (height * height)

# Display BMI
print("\nYour BMI is:", round(bmi, 2))

# BMI Categories
if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal Weight")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")