import math
solvefor = input('solving for: ')
   
if solvefor=="a":
    b = float(input('variable b: '))
    c = float(input('variable c: '))
    print(round(math.sqrt((c**2)-(b**2)),2))
elif solvefor=="b":
    a = float(input('variable a: '))
    c = float(input('variable c: '))
    print(round(math.sqrt((c**2)-(a**2)),2))
elif solvefor=="c":
    a = float(input('variable a: '))
    c = float(input('variable b: '))
    print(round(math.sqrt((a**2)+(b**2)),2))
else:
    print('enter a, b or cc and try again')
