using JuMP, Gurobi

m = Model(Gurobi.Optimizer)

@variable(m, Y[2:3,12:15], Bin)
@variable(m, RM[11:15] >= 0) # (RM) Raw Milk produced
@variable(m, PMD[12:15] >= 0) #  (PMD) Premium Milk Demand
@variable(m, 0 <= RMO[12:15] <= 25000) # constraint: cannot purchase more raw milk 
                                     # than what other dairies can offer
                        # (RMO) raw milk processed into premium milk

@variable(m, BP[11:15] >= 0) # (BP) Butter Produced
@variable(m, BM[11:15] >= 0) # (BM) Butter procured from Market
@variable(m, BI[11:15] >= 0) # (BI) Butter Inventory

@variable(m, BRC[11:15] >= 0) # (BRC) Butter used for ReCommbination
@variable(m, SMPP[11:15] >= 0) # (SMPM) Skimmed Milk Powder Produced
@variable(m, SMPM[11:15] >= 0) # (SMPM) Skimmed Milk Powder procured from Market
@variable(m, SMPI[11:15] >= 0) # (SMPI) Skimmed Milk Powder Inventory

@variable(m, SMPRC[11:15] >= 0) # (SMPRC) SMP used for ReCommbination

@variable(m, PM[12:15] >= 0) # (PM) Premium Milk Final Production
@variable(m, PMS[12:15] >= 0)  # (PMS) premium milk sold 
@variable(m, PMI[11:15] >= 0) # (PMI) Premium Milk Inventory

@variable(m, PMRC[12:15] >= 0) # (PMRC) premium milk recombination
@variable(m, YBI[12:15], Bin) # (YBI) holding cost: refirgerating cost if butter is stored
# @variables(m, RCO[11:15] >= 0)

# Input data: initial raw milk inventory and projected daily supply of raw milk from farmers
setRM = [12110/0.05, 223350, 249689, 232867, 249313]
@constraint(m, fixRM[t=11:15], RM[t] == setRM[t-10])

# Input data: Initial inventory of SMP and butter
@constraint(m, SMPI[11] == 1200) 
@constraint(m, BI[11] == 520)

# Initialization of all variables
@constraint(m, BRC[11] == 0)
@constraint(m, SMPRC[11] == 0)
@constraint(m, BP[11] == 0)
@constraint(m, BM[11] == 0)
@constraint(m, SMPP[11] == 0)
@constraint(m, SMPM[11] == 0)
@constraint(m, PMI[11] == 0)

# Objective: maximize profit

# ?? SMPM vs SMPP

@objective(m, Max, sum(22*PMS[t] - 15*RM[t] - 
        4*(0.95*RM[t] + 0.05*RM[t-1]) - 20.5*RMO[t] - 
        21*PMRC[t] - 2500*YBI[t] - 163*SMPM[t] - 112*BP[t] 
        for t=12:15))

# For 1 liter:
# Premium milk sold generates INR22
# Procurement from collection centers INR15; Processing INR4
# Procurement from other dairies INR16.5; Processing INR4
# Recombination costs INR21
# If butter is stored, cost is INR2500
# SMP and butter costs are INR163/kg and INR112/kg respectively
# Cannot sell more than demand

@constraint(m, Const2a[t=12:15], PMS[t] <= PMD[t] )
@constraint(m, Const2b[t=12:15], PMS[t] >= 0.95*PMD[t] )

# Production quantity
@constraint(m, Const3[t=12:15], PM[t] == 0.95*RM[t] + 0.05*RM[t-1] - 
    1000/93.45*SMPP[t] - 1000/54.87*BM[t] + RMO[t] + PMRC[t] + PMI[t-1] )

# Premium milk produced on day t is
# 95% of daily raw milk procurement
# +5% of raw milk procured on day t-1
# -Liters used to produce SMP: 1000 liters produce 93.45kg SMP
# -Liters used to produce butter: 1000 liters produce 54.87kg butter
# +Raw milk procured from other dairies
# +Premium milk produced from recombination
# +Premium milk inventory carried over from day t-1


# Cannot sell more than produced
@constraint(m, Const4b[t=12:15], PMS[t] <= PM[t] )

# Inventory balance for premium milk: count inventory at the end of a day
@constraint(m, Const5[t=12:15], PMI[t] == PM[t] - PMS[t] )

# SMP produced with a minimum quantity
@constraint(m, Const6[t=12:15], SMPP[t] >= 3738*Y[2,t] )
# SMP produced only with at least 40K liters of excess raw milk -> min quantity produced = 40*93.45kg
@constraint(m, Const6b[t=12:15], SMPP[t] <= 10^9*Y[2,t] )
# Big M constraint: if we do not produce SMP, then the quantity should be 0

# Butter produced with a minimum quantity 
@constraint(m, Const7[t=12:15], BM[t] >= 1097.4*Y[3,t] )
# butter produced only with at least 20K liters of excess raw milk -> min quantity produced = 20*54.87kg
@constraint(m, Const7b[t=12:15], BM[t] <= 10^9*Y[3,t] )
# Big M constraint: if we do not produce butter, then the quantity should be 0


# Recombination requires certain proportions of SMP and butter
@constraint(m, Const8[t=12:15], SMPRC[t]/93.45 - BRC[t]/54.87 == 0 )
@constraint(m, Const9[t=12:15], PMRC[t] == 1000*SMPRC[t]/93.45 + 1000*BRC[t]/54.87 )

# Butter and SMP used in recombination cannot be more than the amount available
@constraint(m, Const10[t=12:15], SMPRC[t] <= SMPI[t-1] + SMPP[t] + SMPM[t] )
@constraint(m, Const11[t=12:15], BRC[t] <= BI[t-1] + BP[t] + BM[t] )

# Inventory balance for SMP and butter: count inventory at the end of a day
@constraint(m, Const12[t=12:15], SMPI[t] == SMPI[t-1] + SMPP[t] + SMPM[t] - SMPRC[t] )
@constraint(m, Const13[t=12:15], BI[t] == BI[t-1] + BP[t] + BM[t] - BRC[t] )

# Capacity constraint on storing butter
@constraint(m, Const14[t=12:15], BI[t] <= 10000*YBI[t] )


optimize!(m)



# Output
println("\nObjective value: ", objective_value(m)) #3.0282e6

println("\nSales and demand: ")
println("Total premium milk sold: ", value.(PMS))
println("Total premium milk demanded: ", value.(PMD))

println("\nProduction: ")
println("Total premium milk produced: ", value.(PM))
println("Premium milk produced from recombination: ", value.(PMRC))
println("SMP used for recombination: ", value.(SMPRC))
println("Butter used for recombination: ", value.(BRC))
println("SMP produced: ", value.(SMPM))
println("Butter produced: ", value.(BM))

println("\nProcurement: ")
println("Raw milk procured from other dairies: ", value.(RMO))
println("SMP purchased from market: ", value.(SMPP))
println("Butter purchased from market: ", value.(BP))

println("\nInventory: ")
println("Premium milk inventory carried over: ", value.(PMI))
println("SMP inventory carried over: ", value.(SMPI))
println("Butter inventory carried over: ", value.(BI))

println("\nBinary decisions: ")
println("Is SMP produced? ", value.(Y[2,:]))
println("Is butter produced? ", value.(Y[3,:]))
println("Is butter inventory carried over? ", value.(YBI))


