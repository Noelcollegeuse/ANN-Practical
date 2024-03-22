import numpy as np
class myFuzzySet:
    def __init__(self, a, b, c):
        self.a = a  # Left
        self.b = b  # Center
        self.c = c  # Right
 
    def membership(self, x):
        if x <= self.b:
            return (x - self.a) / (self.b - self.a)
        elif x <= self.c:
            return (self.c - x) / (self.c - self.b)
        else:
            return 0
    def area(self):
        return (self.c - self.b)
 
temperature_below_average = myFuzzySet(15, 30, 45)
temperature_low = myFuzzySet(-5, 10, 25)
pressure_below_average = myFuzzySet(1.25, 2 ,2.75)
pressure_low = myFuzzySet(0.25 , 1, 1.75)
heating_power_medium_high = myFuzzySet(3.25, 4 ,4.75)
heating_power_high = myFuzzySet(4.25, 5, 5.75)
valve_opening_medium_low = myFuzzySet(1.25, 2 , 2.75)
valve_opening_small = myFuzzySet(0.25,  1, 1.75)
 
temperature_input = 16.5
pressure_input = 1.3
z1 = min(temperature_below_average.membership(temperature_input), pressure_below_average.membership(pressure_input))
z2 = min(temperature_low.membership(temperature_input), pressure_low.membership(pressure_input))
print("z1 =", z1)
print("z2 =", z2)
 
c1num = (z1*heating_power_medium_high.area()*heating_power_medium_high.b)+(z2*heating_power_high.area()*heating_power_high.b)
c2num = (z1*valve_opening_medium_low.area()*valve_opening_medium_low.b)+(z2*valve_opening_small.area()*valve_opening_small.b)
c1den = (z1*heating_power_medium_high.area()+z2*heating_power_high.area())
c2den = (z1*valve_opening_medium_low.area()+z2*valve_opening_small.area())
c1 = c1num/c1den
c2 = c2num/c2den
print("C1 and C2 =", c1,c2)