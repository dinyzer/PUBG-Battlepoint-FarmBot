coords = input("""Select one resolution and the input.txt will be created

1- 1920x1080
2- 1366x768
3- 2560x1440
4- 1680x1050
""")
x1=0.5302083333333333
y1=0.5759259259259259
x2=0.8916666666666667
y2=0.8814814814814815
x3=0.4989583333333333
y3=0.5583333333333333

uno_x1 = 1920*x1
uno_y1 = 1080*y1
dos_x1 = 1366*x1
dos_y1 = 768*y1
tres_x1 = 2560*x1
tres_y1 = 1440*y1
cuatro_x1 = 1680*x1
cuatro_y1 = 1050*y1
uno_x2 = 1920*x2
uno_y2 = 1080*y2
dos_x2 = 1366*x2
dos_y2 = 768*y2
tres_x2 = 2560*x2
tres_y2 = 1440*y2
cuatro_x2 = 1680*x2
cuatro_y2 = 1050*y2
uno_x3 = 1920*x3
uno_y3 = 1080*y3
dos_x3 = 1366*x3
dos_y3 = 768*y3
tres_x3 = 2560*x3
tres_y3 = 1440*y3
cuatro_x3 = 1680*x3
cuatro_y3 = 1050*y3

try:
	coordint = int(coords)
except:
	print("The input string can´t be converted to an Integer")
if coordint == 1:
	file = open('input.txt', 'w',encoding="utf-8")
	uno1 = str(uno_x1) + " "+str(uno_y1)+"\n"
	uno2 = str(uno_x2)+" "+str(uno_y2)+'\n'
	uno3 = str(uno_x3)+" "+str(uno_y3)+"\n"
	file.write(uno1)
	file.write(uno2)
	file.write(uno3)
	print("input.txt created for 1920x1080")
elif coordint == 2:
	file = open('input.txt', 'w',encoding="utf-8")
	dos1 = str(dos_x1) + " "+str(dos_y1)+"\n"
	dos2 = str(dos_x2)+" "+str(dos_y2)+'\n'
	dos3 = str(dos_x3)+" "+str(dos_y3)+"\n"
	file.write(dos1)
	file.write(dos2)
	file.write(dos3)
	print("input.txt created for 1366x768")
elif coordint == 3:
	file = open('input.txt', 'w',encoding="utf-8")
	tres1 = str(tres_x1) + " "+str(tres_y1)+"\n"
	tres2 = str(tres_x2)+" "+str(tres_y2)+'\n'
	tres3 = str(tres_x3)+" "+str(tres_y3)+"\n"
	file.write(tres1)
	file.write(tres2)
	file.write(tres3)
	print("input.txt created for 2560x1440")
elif coordint == 4:
	file = open('input.txt', 'w',encoding="utf-8")
	cuatro1 = str(cuatro_x1) + " "+str(cuatro_y1)+"\n"
	cuatro2 = str(cuatro_x2)+" "+str(cuatro_y2)+'\n'
	cuatro3 = str(cuatro_x3)+" "+str(cuatro_y3)+"\n"
	file.write(cuatro1)
	file.write(cuatro2)
	file.write(cuatro3)
	print("input.txt created for 1680x1050")
else:
	print("You didn´t have selected one of the numbers, open this program again")