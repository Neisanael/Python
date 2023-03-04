print("===================================================================")
mass_of_water = float(input("Enter mass of some water : "))
temperature = float(input("Enter the temperaature change from the user : "))
total_amount_of_energy = mass_of_water * 4.186 * temperature
print("Total Amount of Energy is ",total_amount_of_energy,)
kilo_watt = total_amount_of_energy / 2.77778e-7
electricity_cost = kilo_watt * 9.8
print("cost electricity is ",electricity_cost) 
print("===================================================================")