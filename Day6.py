x = int(input("ENTER X COORDINATE"))
y = int(input("ENTER Y COORDINATE"))

if (x>0 and y>0):
    print(f'{x} & {y} are in 1st Quadrant')

elif (x<0 and y>0):
    print(f'{x} & {y} are in 2nd Quadrant')

elif (x<0 and y<0):
    print(f'{x} & {y} are in 3rd Quadrant')

elif (x>0 and y<0):
    print(f'{x} & {y} are in 4th Quadrant')

elif ((x==0) and (y>0 or y<0)):
    print(f'{x} & {y} are on Y axis line')

elif ((y==0) and (x>0 or x<0)):
    print(f'{x} & {y} are on X axis line')

else:
    print(f' {x} & {y} are on Origin')