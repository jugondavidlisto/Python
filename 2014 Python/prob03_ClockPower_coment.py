#!/usr/bin/env python

#CodeWars 2014
#
#Clock Power
# 
# The clock uses four seven-segment LEDs to display the hours and 
# the minutes. Lighting a single segment of an LED requires 15 milliamps. 
# There is also a divider between the hours and the minutes. 
# Lighting the divider requires 20 milliamps. 
# The first LED for the hours portion of the clock will be unlit 
# for hour values less than 10.
#
# Given a time value, output the number of milliamps required to 
# light the clock.
#
#Input:
# Input begins with a single integer T (0 < T < 50) representing the 
# number of time values. The following T lines will contain a single 
# time value of the format HH:MM. The HH value will be a number 
# between 1 and 12, inclusive. There will be no leading zero for 
# hour values less than 10. The MM value will be a number between 
# 0 and 59, inclusive. The MM value will have a leading zero for 
# values less than 10.
#
# 6
# 1:23
# 10:58
# 12:00
# 3:14
# 1:11
# 8:38
#
# Output:
#
# For each time value, output the number of milliamps required.
#
# 200 milliamps
# 320 milliamps
# 305 milliamps
# 185 milliamps
# 110 milliamps
# 305 milliamps
# 

import sys		#Importa la funció de sistema per la lectura

#Defineix el valor de cada un dels nombres encesos
def digitAmps (digit):
    if (digit == 1):
        return 30
    elif ( (digit==2) or (digit==3) or (digit==5)):
        return 75
    elif (digit==4):
        return 60
    elif ((digit==6) or (digit==9) or (digit==0)):
        return 90
    elif (digit==7):
        return 45
    else: #only 8 is left
        return 105

#Demana que introduim els valors en linies separades

print ("Enter count of times, then those times on separate lines.")
loopCount = int(sys.stdin.readline())	#llegeix nombre de linies
while (loopCount > 0):		#Mentre la linia sigui >0
    loopCount -= 1		#Descompte una linia al total
    line = sys.stdin.readline()		#llegeix la linia
    totalAmps=20  #Valor inicial de la separacio de cifres
    for c in line:	#bucle mentre hi ha linies
        if c.isdigit():	#Determina si és un nombre
            totalAmps += digitAmps(int(c))	#Suma el valor del nombre que veu
    print (totalAmps, "milliamps")	#mostra el resultat per pantalla
