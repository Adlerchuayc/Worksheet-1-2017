print("If you do not type the right stuff, the program will not work!!")



#quantity
i_quantity = float(int(input("Input a quantity:  ")))


    
#length area or volume
i_lav = input("Select either length, area or volume:  ")
if i_lav.lower() == "length":
    power = 1
elif i_lav.lower() == "area":
    power = 2
elif i_lav.lower() == "volume":
    power = 3

#input base unit
i_unit = input("Select the base unit of measurement  (mm, cm, m, km) :  ")
if i_unit.lower() == "mm":
    a = 0.001
elif i_unit.lower() == "cm":
    a = 0.01
elif i_unit.lower() == "m":
    a = 1.0
elif i_unit.lower() == "km":
    a = 1000.0


#output base unit
o_unit = input("Select which base unit of measurement to convert to  (mm, cm, m, km) :  ")
b = o_unit
if o_unit.lower() == "mm":
    b = 0.001
elif o_unit.lower() == "cm":
    b = 0.01
elif o_unit.lower() == "m":
    b = 1.0
elif o_unit.lower() == "km":
    b = 1000.0
    
#conversion
if i_unit.lower() == o_unit.lower():
    o_quantity = i_quantity
else:
    o_quantity = (i_quantity) * (a / b ** power)
    



INPUT = str(int(i_quantity)) + " " + i_unit + "^" + str(power)
EQUAL = " = "
OUTPUT = str(int(o_quantity)) + " " + o_unit + "^" + str(power)
print(INPUT + EQUAL + OUTPUT)
