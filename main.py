# Author: Chang Li cxl5844@psu.edu
# Collaborator: Yangling Wang yuw17@psu.edu

Tem= input("Enter temperature: ")
Tem=float(Tem)
Typ=input("Enter unit in F/f or C/c: ")
if Typ=='C' or Typ=='c': 
  print(str(Tem)+"° in Celsius is equivalent to "+str(Tem*1.8+32.0) +"° Fahrenheit.")
elif Typ =='F' or Typ=='f': 
  print(str(Tem)+"° in Fahrenheit is equivalent to "+str((Tem-32.0)/1.8) +"° Celsius.")
else: 
  print(f"Invalid unit({Typ}).")