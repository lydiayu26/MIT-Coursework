def part_c(initial_deposit):
	
	total_cost = 950000.0
	portion_down_payment = 0.32 * total_cost
	steps = 0
	
	L = 0
	H = 10000
	r = (L+H)/2
	best_r = r/10000.0
	
	execute = True
	
	current_savings = initial_deposit*(1 + best_r/12)**36
	
	if initial_deposit*(1+1.0/12)**36 < portion_down_payment:
	    execute = False
	    best_r = 'It is not possible to pay the down payment in three years.'
	
	while execute and abs(current_savings - portion_down_payment) > 100:  
	    steps += 1
	    if current_savings > portion_down_payment:
	        H = r
	    else:
	        L = r
	    r = (H+L)/2
	    best_r = r/10000.0 
	    current_savings = initial_deposit*(1 + best_r/12)**36
	
	print("Best savings rate:", best_r)
	print("Steps in bisection search:", steps)
	return best_r, steps