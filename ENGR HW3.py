##########################################################################################
# Program Filename: ENGR 103 - HW 3
# Author: Jeyeong You
# Date: 05.11.22
# Description: Calculate the sediment settling velocity, water retention time,
# and energy savings using a dry pond stormwater management system.
# Input:sediment grain size
# Output: Settling velocity, Time to settle in a 2m depth pond, Diameter of orifice, The energy savings
##########################################################################################

# Importing libraries
import numpy as np
import math

# Part 1 : the settling velocity of the sediment grain sizes
print('---------------------------------------------Part1----------------------------------------------------')

# Settling Velocity Variable
ps = 2650  # sediment density (kg/m^3)
p = 1000  # water density (kg/m^3)
μ = 1E-3  # dynamic viscosity of the fluid (Ns/m^2)
g = 9.81  # acceleration due to gravity (m/s^2)

# List
grain_size = [10, 20, 30, 40, 50, 60]

# settling velocity
for d in grain_size:
    guess_ws = 10
    calculated_ws = 15
    difference = calculated_ws - guess_ws
    while (difference > 0.000000001):
        rep = (p * d * 0.000001 * guess_ws) / μ  # The particle Reynolds number equation
        cd = 1.4 + (36 / rep)    # The drag coefficient on the sediment grains equation
        calculated_ws = np.sqrt(4 / 3 * (g * d * 0.000001 /cd) * ((ps/p)-1))   # Settling velocity of the sediment equation
        difference = guess_ws - calculated_ws
        guess_ws = calculated_ws
    print('Settling velocity:\n', d, 'micrometers =', calculated_ws, 'm/s.')

print( )

# Part 2 : Time to settle in a 2m depth pond
print('----------------------------------------------Part2--------------------------------------------------')
for d in grain_size:
    guess_ws = 10
    calculated_ws = 15
    difference = calculated_ws - guess_ws
    while (difference > 0.000000001):
        rep = (p * d * 0.000001 * guess_ws) / μ  # The particle Reynolds number equation
        cd = 1.4 + (36 / rep)  # The drag coefficient on the sediment grains equation
        calculated_ws = np.sqrt(
            4 / 3 * (g * d * 0.000001 / cd) * ((ps / p) - 1))  # Settling velocity of the sediment equation
        difference = guess_ws - calculated_ws
        guess_ws = calculated_ws
    time = 2 / calculated_ws / 3600
    print('Time to settle in a 2m depth pond:\n For', d, 'micrometer grain size sediments it takes', round(time,2) , 'hours to settle in the pond.')
print( )

# Part 3 : The needed orifice size
print('----------------------------------------------Part3--------------------------------------------------')
# Time to settle Variable
_A = 200 * 200  # surface area(A) of the pond
c = 0.98  # the orifice discharge coefficient
g = 9.81  # acceleration due to gravity (m/s^2)
h_i = 2  # the initial water height (m)
h_f = 0  # the final water height (m)
t = 1.03  # based on part 2

d_pipe = np.sqrt((_A * 4) / (math.pi * t * 3600  * c) * (np.sqrt(h_i) - np.sqrt(h_f)) * np.sqrt(2/g))  # pipe diameter equation
print('The orifice needs to be', round(d_pipe, 2), 'm in diameter to allow 85% of the sediments in the pond to settle before the water leaves the pond.')
print( )

# Part 4 : The energy savings in terawatt hours and in $
print('----------------------------------------------Part4--------------------------------------------------')
# saving energy calculation = Total energy - 90% energy(waste water)
total_electricity_usage = 1875  # megawatt-hours
wastewater_electricity_usage = 1875 * 0.90 # megawatt-hours
energy = (total_electricity_usage - wastewater_electricity_usage) * 1E-6  # 1E-6 is to convert mega to tera (twh)

# saving money calculation = Total money - 90% money(waste water)
total_money_usage = 1875 * 1000 * 0.116  # convert 1875 Mwh to kwh and then multiply by 0.116/kwh
wastewater_money_usage = 1875 * 0.90 * 1000 * 0.116
money = total_money_usage - wastewater_money_usage

print('The energy savings of removing 10% of the water being processed \n unnecessarily '
      'by the Corvallis wastewater treatment plant is',energy, 'twh and will save the city $',money,'per year.')