# Problem set 1a
# Name: Lydia Yu
# Collaborators: 
# Time Spent: 0.5 hrs

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.18
current_savings = 0.0
r = 0.03
months = 0

while current_savings < (total_cost * portion_down_payment):
    current_savings += (portion_saved * (annual_salary/12)) + (current_savings * r/12)
    months += 1
    
print("Number of months:", months)