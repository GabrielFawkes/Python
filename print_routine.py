#!/usr/bin/python
y = [0] * 312
tmp = y[0]
for i in range(0,310):
    if i % 2 == 0:
        y[i] = tmp + 0.03472
    else:
        y[i] = tmp + 0.03611
    tmp = y[i]
    print (y[i])

for j in range(0,310):
    y[j]=str(y[j])[:7]
    print (y[j])
y[0] = 0
fil = open("print_routine.ngc", "w")
fil.write ("G17 G20 G40 G49 \n")
fil.write ("G54 G80 G90 G94 \n")
fil.write ("G00 X0 Y0 F50 \n")
fil.write ("G01 X9 Y0 F700 \n")
fil.write ("G01 X9 Y0.03472 F50 \n")
fil.write ("G01 X0 Y0.03472 F700\n")

for k in range(0, 310):
    if k%2 == 1:
        fil.write ("G01 X9 Y")
        fil.write (str(y[k]))
        fil.write (" F700 \n")
        fil.write ("G01 X9 Y")
        fil.write (str(y[k+1]))
        fil.write (" F50 \n")
    else:
        fil.write ("G01 X0 Y")
        fil.write (str(y[k]))
        fil.write (" F700 \n")
        fil.write ("G01 X0 Y")
        fil.write (str(y[k+1]))
        fil.write (" F50 \n")


fil.close()

#for k in range(0,310)