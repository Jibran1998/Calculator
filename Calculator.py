import re
import pyfiglet
from termcolor import colored

def calculate():
    global previous
    if previous == 0:
        equation = input(">>")
    else:
        equation=input(f"{previous}>>")
    if equation in ("quit","q"):
        exit()
    elif equation=="0":
        previous=0
    else:
        equation= re.sub('[a-z A-Z,"()!@^&]'," ",equation )
        if previous==0:
            previous=eval(equation)
        else:
            if equation[0] not in ('+','-','*','/','%'):
                previous = eval(equation)
            else:
                previous = eval(str(previous) + (equation))



banner = pyfiglet.figlet_format("Calculator")
banner = colored(str(banner), 'red')
print(f"\t\t{banner}")
print("-----------------------------------------------------")
print("Enter q or quit to quit the program")
print("-----------------------------------------------------")
print("\nEnter the equations")
previous = 0
run = True

while run:
    calculate()