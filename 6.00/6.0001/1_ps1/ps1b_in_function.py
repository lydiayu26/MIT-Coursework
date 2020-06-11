def part_b(annual_salary, portion_saved, total_cost, semi_annual_raise):
	
	portion_down_payment = 0.18
	current_savings = 0.0
	r = 0.03
	months = 0
	
	while current_savings < (total_cost * portion_down_payment):
	   if months % 6 == 0 and months != 0:
	       annual_salary += annual_salary * semi_annual_raise
	   current_savings += (portion_saved * (annual_salary/12)) + (current_savings * r/12)
	   months += 1
	    
	print("Number of months:", months)
	return months