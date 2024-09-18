#https://www.w3schools.com/python/ref_math_pi.asp
#https://www.w3schools.com/python/ref_func_pow.asp
import math

rad=float(input("Please enter the radius of the circle\n"))

diameter=rad*2
print("The diameter is %d\n"%(diameter))
print("---------------------------------------")

circumference=2*math.pi*rad

print("The circumference  is %.2f\n"%(circumference  ))

print("---------------------------------------") 

area=math.pi*pow(rad,2)
print("The area   is %.2f\n"%(area ))
